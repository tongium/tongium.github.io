---
layout: post
title: "After the AI Bubble: Could a Human Salary Be Cheaper Than Tokens?"
date: 2026-11-09 09:00:00 +0700
tags: [technology, AI, economics, software engineering, careers]
description: "Today's AI tokens are priced with venture money. If the bubble pops and prices move toward their true cost, could hiring a person become cheaper than running an agent? Some rough math, from Bangkok."
image: /assets/images/og/human-salary-vs-tokens.png
---

Every few weeks someone shares a screenshot of their AI bill.

$400. $1,800. $6,000 for one month, from one engineer, running agents in a loop. And the comment underneath is always the same: "Still cheaper than hiring someone."

That line deserves a second look. Because the price on that bill isn't a law of physics. It's a price. And prices in a bubble have a habit of being wrong.

So here's the question I keep coming back to: **if the AI bubble crashes, could a human salary end up cheaper than tokens?**

---

### Why Tokens Feel Cheap Right Now

The price you pay per million tokens is not the cost of making them.

Behind every API call there are GPUs that cost tens of thousands of dollars each, data centers that need their own power deals, cooling, networking, and teams of very well-paid researchers. A lot of that is being paid for by venture capital and by the capex budgets of a few very large companies, all racing for market share.

That's not a conspiracy. It's the normal playbook. Ride-hailing was cheap while investors paid for it. Food delivery was cheap while investors paid for it. Then the money wanted a return, and prices went up.

AI is running the same playbook at a much bigger scale. To be fair, the per-token API price usually does cover the cost of *running* the model. What it doesn't cover is the billions spent *training* it, and the data centers built ahead of demand. And the flat-rate "unlimited" plans many of us use are almost certainly losing money on their heaviest users. Winning the developer habit today is worth more than margin today.

When a bubble pops, the subsidy is the first thing to go.

---

### Agents Don't Sip Tokens

The second half of the problem is how we use them now.

A chat is cheap. You ask a question, you get an answer, maybe a few thousand tokens. An **agent** is a different animal. It reads the repo, runs the tests, reads the failures, tries a fix, re-reads the files, runs the tests again. Every turn re-sends a big chunk of context.

Ten turns over a 100k-token context isn't 100k tokens. It pushes a million tokens through the pipe. Prompt caching discounts most of that, but do it twenty times a day and one engineer is still churning through tens of millions of tokens, every day.

We moved from paying per question to paying per *attempt*. And agents make a lot of attempts.

---

### The Math Nobody Wants to Do

Rough numbers. These are my assumptions, not facts. Swap in your own.

**The agent side:**

*   One engineer runs coding agents through a normal working day.
*   Around **250 million tokens a month**, most of it cached context, some fresh input, a bit of output.
*   At today's prices, with caching doing a lot of the work, that lands somewhere around **$1,000 a month**. Heavier users pay more. Lighter users pay less.

**The human side (junior developer, full monthly cost):**

| | Monthly cost (approx.) |
|---|---|
| San Francisco | $11,000 – $14,000 |
| Bangkok | $1,100 – $1,600 (base salary about 30,000 – 45,000 THB, plus overhead) |

**Now pop the bubble.** Say prices move toward real cost and the same workload costs 3× to 5× more:

| Scenario | Agent bill per month | Agent vs. SF junior | Agent vs. Bangkok junior |
|---|---|---|---|
| Today | ~$1,000 | ~10× cheaper | about the same |
| Post-crash (3×) | ~$3,000 | ~4× cheaper | ~2–3× **more expensive** |
| Post-crash (5×) | ~$5,000 | ~2.5× cheaper | ~3–4× **more expensive** |

Look at the last column.

In San Francisco, even a painful price correction leaves the agent far cheaper than a person. In Bangkok, the agent is *already* at roughly the same cost as a junior developer. After a correction, the person wins on price by a wide margin.

So the honest answer to the title is: **it depends where you're standing.** And from where I'm standing, the answer is "yes, quite possibly."

---

### The Case Against Me

I asked Gemini to argue the other side, and it made good points. Here's the strongest version.

**1. The crash might make tokens cheaper, not more expensive.**
When the dot-com bubble burst, it left behind miles of "dark fiber": cables laid by bankrupt companies, later bought for pennies. That cheap bandwidth helped power the next decade of the internet. An AI crash could do the same with GPUs. Bankrupt neoclouds sell their clusters at fire-sale prices, and inference gets cheaper overnight.

My one pushback: fiber lasts decades. GPUs are worn out, or outclassed, in three to five years. A fire sale helps for a while. It doesn't last a generation.

**2. You don't need a frontier model to write a CRUD endpoint.**
Small open-weight models are getting very good. A lot of everyday coding work, the boring parts, can run on a decent local machine for the price of electricity. The bubble is mostly in the frontier labs. The small models don't care if it pops.

**3. Efficiency keeps compounding.**
Prompt caching, distillation, speculative decoding, custom chips. Every year the same answer costs less to produce. A price spike would be fighting a strong downward trend.

All fair. I think the most likely outcome is a **split market**: commodity tokens get cheap, frontier tokens get expensive. Which means the expensive part is exactly the part we lean on for the hard work.

---

### It Was Never Really "Agent vs. Human"

Here's where the comparison breaks down, and I think it's the more important point.

Nobody is actually choosing between one agent and one junior developer. The agent doesn't own anything. It doesn't go to the meeting, it doesn't remember last quarter's incident, and somebody still has to read what it writes. (I wrote about what happens when nobody does in [PR Storm]({% post_url 2026-11-03-pr-storm %}).)

The real choice is between:

*   **A senior engineer + a big token budget**, or
*   **A senior engineer + a junior + a smaller token budget.**

And the junior has one thing tokens don't: **they compound.** Every month, they get better at your codebase, your customers and your mistakes. In two years they're the senior. Tokens you spend today buy you nothing next year except a bill.

A company that stops hiring juniors because tokens are cheaper isn't saving money. It's skipping the step where it grows its next set of seniors. That's a debt, and it comes due at the worst possible time, probably right around when the token price goes up.

---

### The Uncomfortable Bit

For a long time, "AI will replace developers" has been told from a Silicon Valley point of view, where a junior costs six figures and almost anything looks cheap next to that.

But most of the world's developers don't earn San Francisco salaries. In Bangkok, Manila, Ho Chi Minh City or Nairobi, the math was never as obvious. A post-crash price correction could flip it entirely, and we might get a strange outcome: **heavy AI automation becomes a luxury of expensive cities, while cheaper cities quietly keep hiring people.**

I'm not sure that's a happy story either. It's a story where people are competitive because they're cheap. That's not the same as being valued.

---

### What I'd Actually Do

*   **Know your real token cost per outcome**, not per month. "$2,000 on tokens" means nothing. "$40 per merged, reviewed feature" means something.
*   **Don't build a team that only works at today's prices.** If your plan breaks at 3× the token cost, it's not a plan, it's a bet.
*   **Use small models for small jobs.** Save the frontier models for the work that actually needs them.
*   **Keep hiring juniors.** Not out of kindness. Out of self-interest.
*   **If you're early in your career outside a rich tech hub**, the gap between "a person who uses AI well" and "an AI bill" is your opportunity. Be the first one.

---

### The Short Version

*   Today's token prices are partly paid for by investors. That won't last forever.
*   Agents burn tokens at a rate chats never did.
*   After a correction, a junior in San Francisco is still more expensive than an agent. A junior in Bangkok probably isn't.
*   A crash could also flood the market with cheap GPUs, so don't bet everything on prices rising.
*   The real comparison isn't agent vs. human. It's what your team looks like in two years.

Tokens are cheap the way a free trial is cheap. The bill was always coming. The only question is who's holding it when it arrives.

---

*Co-written with Gemini, which argued the case against me with more enthusiasm than I expected. The numbers are rough and the opinions are mine.*
