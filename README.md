# StyleBot
StyleBot enforces style guide rules by automating term-checking.

## Inspiration
### Style guide? What's that?
When I join a technical publications team for the first time, a key question I ask is:

>"Is there a style guide?"

Often times, the team raise their eyebrows, smile sheepishly, and shrug.

>"Yeah... about that."

The team agrees that having a style guide is an important resource for any writing team. A well-designed and implemented style guide improves the quality, and in particular the clarity, of documentation. It unifies distinct writing projects under a single, consistently-branded voice. It answers a lot of questions up front and eliminates of circular debates over whether we should be writing like *this* or like *that*. Applying a style guide early in the life of a doc set cuts costs on maintenance and retroactive style application, because it would be done correctly (or at least *consistently*) the first time around.

And many a team gather in tech pubs summits to duke out their opinions and reasonings, battle royale style, once and for all. In addition, resources like the [IBM Style Guide](https://www.amazon.com/IBM-Style-Guide-Conventions-Writers/dp/0132101300/ref=sr_1_1?ie=UTF8&qid=1522430954&sr=8-1&keywords=ibm+style+guide) and [Chicago Manual of Style](https://www.amazon.com/Chicago-Manual-Style-17th/dp/022628705X/ref=sr_1_1?ie=UTF8&qid=1522432166&sr=8-1&keywords=chicago+manual+of+style) provide a sturdy foundation of rigorously-tested, industry-vetted style guide best practices so that no well-informed and well-read team has to start completely from scratch.

### It sounds like a good idea, but...

Many well-meaning tech pubs teams try to enforce a newly-established style guide at first. However, as under-resourced teams that rely heavily on first-pass quality and peer review, and that *also* face Very Aggressive Deadlines, these same teams end up flinging the style guide out the window soon enough. It's just not practical or sustainable.

The result? Failure to standardize and one-voice across documents. Difficulty upkeeping the whole doc set to ever-changing parameters of an evolving stylesheet. Documents that clearly appear "outdated" within a short time frame. Flagging reader confidence.

### Enter StyleBot

Increasingly, in today's first-to-market economy, we find ourselves needing to rely heavily on automation, or else succumbing to the inevitable quality decay in the product we deliver. Automation provides the opportunity not necessarily to *replace all humans*, but to lets bots to do bot-work *so that the humans can focus on human-work*.

An experienced writer (or automation professional) knows that human presence cannot be taken out of the equation. Without human eyes on the lookout for sanity checks and reasonable results, gibberish outputs may be published into the world without discretion, and lose readership. However, automation gets us ~75% of the way so that the remaining 25% of the work can be done with adequate attention and care.

Here is an example of a project (Rorybot) that has run into the same findings and attempted a similar application:

https://ux.shopify.com/rorybot-automated-content-style-checking-4d42946ae318

https://github.com/Shopify/rorybot

Rorybot is a terms-checking robot that enforces a very specific type of style enforcement called term-checking. If a convention is established for how to notate specific types of information, Rorybot looks for potential violations and corrects them. This standardization for distinct types of information, like date/time notation or product-specific terminology, will provide clarity and simplicity to the content so readers can focus on the content.

## Build Scope
Here is the 5-stage StyleBot build plan.

### Stage 1
1.	**Read the IBM Style Guide**
2.	Categorize standards into distinct types of term-checking problems
3.	Solve at least one instance of each type of problem to create a design pattern
4.	Document each design pattern to be a representative example/tutorial

### Stage 2
1.	Determine what the “core features” are for the initial build (alpha)
2.	Build alpha based on existing design patterns
3.	Expand design patterns as needed
4.	Document alpha build

### Stage 3+
1.	Identify scope of sensible “expansion module”
2.	Create expansions based on existing design patterns
3.	Expand design patterns as needed
4.	Expand or reduce alpha as needed based on common feedback
5.	Document expansion build
6.	Rinse and repeat

### Stage 4
Create a friendly UI that allows non-technical users to configure their stylebots with custom style standards

### Stage 5
Create a feature that allows non-technical users to tag instances of style violations real-time, to expand library as-you-go.
