# Agent contract

- The site is static. No server, no runtime database call.
- Read data from `database` at build time only.
- Never add secrets or personal data.
- Never write to `database`.
- Keep the build deterministic.
