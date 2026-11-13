# Check the hosted mathematics

These helpers compare the exact Git-tracked mathematical source with the actual commit-pinned GitHub renderer at wide and narrow viewport sizes. They retain source inventories, accessible MathML, screenshots and a structured report. A passing structural check still requires visual inspection and scientific review.

The two helper files are unchanged copies from the public MIT-licensed [Quantum Cooling Geometry source](https://github.com/GoGoKo699/Quantum-Cooling-Geometry/tree/eff91c78b24e0c7bfa11f99a3db6de481dea5134/verification/hosted_math), by the same author. Their Git blob identities are `6f36ee03223a82d0075da2fe903f21bc5a45a75b` and `1d3bf9810d0dfadb844a48b354af80f9b66924bc`. The repository's MIT notice applies.

Install Node.js 18 or later, Python 3.10 or later, Git, Playwright and MathJax in a separate temporary dependency directory. The workflow uses Playwright 1.56.1 and MathJax 3.2.1. From a checkout containing the chosen commit, run:

```bash
NODE_PATH=/absolute/runtime/node_modules node verification/hosted_math/capture_hosted_math.cjs \
  --root /absolute/checkout --repository GoGoKo699/Entangled-Causal-Witnesses \
  --revision FULL_COMMIT_SHA --contract verification/hosted_math/text-contract.json \
  --output /absolute/new-empty-report-directory
```

The command opens a fresh unsigned-in browser context and reads public pages. It authenticates to no account and changes no source or settings. Output directories retain failed attempts; a retry uses a new directory or the documented exact-source `--resume-from` mechanism. The CI workflow is restricted to same-repository pull requests with `contents: read`, checks out the exact proposed commit and persists no checkout credential.

The full default page inventory is used, including scientific, learning, reference and verification Markdown. The text contract names selected headline expressions in addition to the complete source/host structural comparison. The stored report identifies the exact revision, tree, page scope and both viewports. CI artifacts are temporary transport, not permanent preservation of a completed review.
