"""Validate provenance and catalog integrity without contacting external sites."""
from __future__ import annotations
import sys
from catalog import load, validate

def main() -> int:
    try:
        data=load()
        errors=validate(*data)
    except (OSError, ValueError, TypeError, KeyError) as exc:
        print(f'Catalog read/shape error: {exc}',file=sys.stderr);return 1
    if errors:
        print('\n'.join(errors),file=sys.stderr);return 1
    print(f'OK: {len(data[0])} records, {len(data[1])} categories. Metadata integrity only; not an external link or scientific-result audit.')
    return 0
if __name__=='__main__':raise SystemExit(main())
