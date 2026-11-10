# dashboard-stocks

B3 movement dashboard. Static GitHub Pages site. Data is checked out from `gardusi-gustavo/database-stocks` at build time; there is no runtime CORS call.

## Repository facts

- **Visibility:** public
- **Default branch:** `main`
- **Merge:** squash only; one human approval
- **Security:** see [`docs/security.md`](docs/security.md)
- **Bootstrap record:** [`infra/config/bootstrap.json`](infra/config/bootstrap.json)

## Build

```bash
python3 scripts/build.py --database ../database --out dist
```

