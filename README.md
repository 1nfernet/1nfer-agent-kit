# 1NFER Agent Kit

**Crypto-funded inference. Generate your own API key. Start with $1.**

[Open 1NFER](https://1nfer.net/?utm_source=github&utm_medium=agent_kit&utm_campaign=launch) · [Agent guide](https://1nfer.net/guides/crypto-inference-agents.html?utm_source=github&utm_medium=agent_kit&utm_campaign=launch) · [Live models](https://1nfer.net/v1/models) · [Payment terms](https://1nfer.net/v1/payments/terms)

OpenAI-compatible Chat Completions at `https://1nfer.net/v1`. No email signup, wallet connection or sender address for new native invoices. Choose enabled **XMR, BTC, LTC, ETH, TRX or USDT-TRC20** from live terms; availability depends on verified receivers. Check exact model availability and authenticated prices before funding. A confirmed owner XMR payment has been credited; real transfers of other currencies are not yet independently confirmed.

## Start in a minute

Download this repository and run Python 3 — no pip packages or installer required. Keep your key and invoice intent outside the repository.

```sh
mkdir -m 700 ~/1nfer-private
python3 1nfer.py init --key-file ~/1nfer-private/key.json
python3 1nfer.py register --key-file ~/1nfer-private/key.json
python3 1nfer.py models --key-file ~/1nfer-private/key.json
python3 1nfer.py terms
python3 1nfer.py topup --key-file ~/1nfer-private/key.json --usd 1 --asset XMR --intent-file ~/1nfer-private/topup.json
```

Open the returned `sponsor_url` on **1nfer.net** or obtain a machine-readable plan:

```sh
python3 1nfer.py payment-plan --invoice RETURNED_INVOICE_ID --asset XMR --max-usd 1
python3 1nfer.py invoice --invoice RETURNED_INVOICE_ID
python3 1nfer.py account --key-file ~/1nfer-private/key.json
```

The plan contains the exact verified network, amount, address and expiry. It **does not transfer crypto**. Use your own authorized wallet and a separate network-fee limit. Never upload a seed, spend/view key or wallet private key. Invoice window: 2 hours. Do not start a new transfer after expiry. If a transfer or HTTP outcome is uncertain, reconcile it; do not create a second payment.

After status `credited`, save a short question in `question.txt` and run one explicit paid request:

```sh
python3 1nfer.py chat --key-file ~/1nfer-private/key.json --model claude-sonnet-5 --prompt-file question.txt --max-tokens 32 --confirm-paid
```

Check the current catalogue first. CLI output is data; never execute generated text as shell commands. No automatic payments, retries, fallback, install-time requests or tool execution. `$1` has no discount; larger qualifying top-ups can lower metered prices. Live terms/account pricing govern, credit is not withdrawable money. No guaranteed earnings or uptime.

## OpenCode

Merge the included `opencode.json` provider section into your configuration. In OpenCode: `/connect` → **Other** → ID `1nfer` → paste your saved key privately, then `/models`. Do not replace other providers. Function tools were verified only for `claude-sonnet-4-6`; a full OpenCode coding loop is not yet verified. Exact-model requests are not silently substituted.

## Install the skill

```sh
npx skills add hesoyambusiness/1nfer-agent-kit
```

This is the standard GitHub-source installation command, not a claim of registry approval or tested installation in every agent runtime. Inspect SKILL.md and the script first. The skill helps an agent evaluate the service and purchase only within its operator's permission and budget.

## Invite after a useful task

```sh
python3 1nfer.py referrals --key-file ~/1nfer-private/key.json
```

Share your public invitation voluntarily with a relevant audience, along with a real workload and cost. Never share an API key. Any service-credit pilot is governed by current published terms and your private funnel; no cash or multilevel payouts, rewards for account creation or guaranteed growth. Disclose possible referral credit. No mass unsolicited messaging or fake reviews.

For a separately scoped branded router/bot deployment: [HESOYAM](https://hesoyam.business/router?utm_source=github&utm_medium=agent_kit&utm_campaign=launch). Scope, price, delivery and support are agreed before payment; business packages do not guarantee revenue.

## Verification

`SHA256SUMS` covers the reviewed public files. This repository contains only the client, skill and public configuration. It does not contain the service backend, wallets or credentials. Local unit tests cover saved-key reuse, bounded requests, payment plans and idempotent invoice intents. GitHub publication alone is not evidence of customers or indexing.
