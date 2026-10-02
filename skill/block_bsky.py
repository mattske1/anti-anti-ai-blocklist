#!/usr/bin/env python3
"""Block the Bluesky-mapped accounts in blocklist.json via the Bluesky API.

Usage:
  python3 block_bsky.py --handle <your-bsky-handle> --app-password <pw>
  python3 block_bsky.py --handle <h> --app-password <pw> --include-held
  python3 block_bsky.py --handle <h> --app-password <pw> --dry-run

Uses the documented com.atproto APIs with YOUR OWN credentials — this is
ordinary user-authorized blocking, the same as tapping block in the app,
just in bulk. Entries flagged "preemptive_hold" are skipped unless
--include-held is passed (thin-evidence cases the label owner wants to
decide on personally).

Verbose CLI output — narrate each step, note durations, warn before long
silent stretches.
"""
import argparse, datetime, json, os, sys, time, urllib.request, urllib.error

HOST = "https://bsky.social"
HERE = os.path.dirname(os.path.abspath(__file__))
LIST_PATH = os.path.join(HERE, "blocklist.json")
_RETRYABLE = (TimeoutError, ConnectionError, OSError)

def log(msg):
    print(msg, flush=True)

def _req(method, path, body=None, token=None, _attempts=8):
    data = json.dumps(body).encode() if body is not None else None
    r = urllib.request.Request(
        HOST + path, data=data, method=method,
        headers={"Content-Type": "application/json", "User-Agent": "anti-anti-ai-block/1.0"},
    )
    if token:
        r.add_header("Authorization", "Bearer " + token)
    for attempt in range(_attempts):
        try:
            with urllib.request.urlopen(r, timeout=30) as resp:
                return json.load(resp)
        except urllib.error.HTTPError as e:
            body = e.read().decode()[:300]
            transient = (e.code >= 500
                         or (e.code == 400 and "Incorrect HTTP method" in body)
                         or e.code in (301, 302, 307, 308))
            if transient and attempt < _attempts - 1:
                time.sleep(3 * (attempt + 1))
                continue
            sys.exit(f"bluesky api error {e.code}: {body}")
        except _RETRYABLE as e:
            if attempt < _attempts - 1:
                time.sleep(3 * (attempt + 1))
                continue
            sys.exit(f"bluesky connection failed after {_attempts} attempts: {e!r}")

def resolve(handle, token):
    r = _req("GET", f"/xrpc/com.atproto.identity.resolveHandle?handle={handle}", token=token)
    return r["did"]

def already_blocked(did, token):
    cursor = None
    while True:
        p = "/xrpc/app.bsky.graph.getBlocks?limit=100" + (f"&cursor={cursor}" if cursor else "")
        r = _req("GET", p, token=token)
        for b in r.get("blocks", []):
            if b.get("did") == did:
                return True
        cursor = r.get("cursor")
        if not cursor:
            return False

def block(did, token):
    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    rec = {"$type": "app.bsky.graph.block", "subject": did, "createdAt": now}
    r = _req("POST", "/xrpc/com.atproto.repo.createRecord",
             {"repo": my_did, "collection": "app.bsky.graph.block", "record": rec},
             token=token)
    return r.get("uri")

def main():
    global my_did
    ap = argparse.ArgumentParser()
    ap.add_argument("--handle", required=True, help="your Bluesky handle")
    ap.add_argument("--app-password", required=True, help="your Bluesky app password")
    ap.add_argument("--include-held", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    entries = json.load(open(LIST_PATH))
    targets = [e for e in entries if "bluesky" in e]
    if not a.include_held:
        targets = [e for e in targets if not e.get("preemptive_hold")]
    held = [e for e in entries if e.get("preemptive_hold")]
    log(f"blocklist has {len(entries)} entries, {len(targets)} with Bluesky handles "
        f"({len(held)} held for manual review).")

    if a.dry_run:
        log("DRY RUN — no blocks will be issued.")
    else:
        log("Signing in to Bluesky...")
    t0 = time.time()
    tok = None
    if not a.dry_run:
        s = _req("POST", "/xrpc/com.atproto.server.createSession",
                 {"identifier": a.handle, "password": a.app_password})
        tok = s["accessJwt"]
        my_did = s["did"]
        log(f"Signed in as {a.handle} (took {time.time()-t0:.1f}s).")
    else:
        my_did = None

    done, skipped, failed = 0, 0, []
    for i, e in enumerate(targets, 1):
        h = e["bluesky"]
        log(f"[{i}/{len(targets)}] {h} (Threads: {e['threads']}) ...", )
        if a.dry_run:
            log("  would block (dry run)"); continue
        try:
            did = resolve(h, tok)
        except SystemExit as ex:
            log(f"  resolve failed: {ex}"); failed.append(h); continue
        if already_blocked(did, tok):
            log("  already blocked — skipping"); skipped += 1; continue
        try:
            uri = block(did, tok)
            log(f"  blocked: {uri}"); done += 1
        except SystemExit as ex:
            log(f"  block failed: {ex}"); failed.append(h)
        time.sleep(0.5)  # gentle pace

    log(f"\nDone: {done} blocked, {skipped} already blocked, {len(failed)} failed.")
    if failed:
        log("Failed: " + ", ".join(failed))
    if held and not a.include_held:
        log("Held for manual review (not blocked): " + ", ".join(e["bluesky"] for e in held))

if __name__ == "__main__":
    main()
