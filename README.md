# StyleBot
StyleBot enforces style guide rules by automating term-checking.

## Inspiration
### Style guide? What's that?
When I join a technical publications team for the first time, a key question I ask is:

>"Is there a style guide?"

Often times, the team raise their eyebrows, smile sheepishly, and shrug.

>"Yeah... about that."

The team agrees that having a style guide is an important resource for any writing team. A well-designed and implemented style guide improves the quality, and in particular the clarity, of documentation. It unifies distinct writing projects under a single, consistently-branded voice. It answers a lot of questions up front and eliminates a lot of circular debates over whether we should be writing like *this* or like *that*. Applying a style guide early in the life of a document set cuts costs on document maintenance and retroactive style application, because it would be done correctly (or at least *consistently*) the first time around.

And many a team gather in tech pubs summits to hash out all their opinions and reasonings once and for all. In addition, resources like the [IBM Style Guide](https://www.amazon.com/IBM-Style-Guide-Conventions-Writers/dp/0132101300/ref=sr_1_1?ie=UTF8&qid=1522430954&sr=8-1&keywords=ibm+style+guide) and [Chicago Manual of Style](https://www.amazon.com/Chicago-Manual-Style-17th/dp/022628705X/ref=sr_1_1?ie=UTF8&qid=1522432166&sr=8-1&keywords=chicago+manual+of+style) provide a sturdy foundation of rigorously-tested, industry-vetted style guide best practices so that no well-informed and well-read team has to start completely from scratch.

### It sounds like a good idea, but...

Most well-meaning tech pubs teams try to enforce the newly-established style guide at first. However as under-resourced teams relying heavily on first-pass quality and peer review that also face Very Aggressive Deadlines, these same teams end up flinging the style guide out the window. It's just not practical.

The result? Failure to standardize and one-voice across documents. Difficulty adapting to ever-changing needs of an evolving stylesheet. Documents that clearly appear "outdated" within a short time frame. Flagging reader confidence.

### Enter StyleBot

Increasingly, in today's first-to-market economy, we find ourselves needing to rely heavily on automation, or else succumb to the inevitable quality decay in our product. Automation provides the opportunity not merely to *replace the humans*, but to create bots to do bot-work *so that the humans can focus on human-work*. Human writers cannot be taken out of the equation. Automation gets us ~75% of the way so that the remaining 25% of the work can be done with adequate attention and care.

Here is an example of a project (Rorybot) that has run into the same findings and attempted a similar application:

https://ux.shopify.com/rorybot-automated-content-style-checking-4d42946ae318

https://github.com/Shopify/rorybot

Rorybot is a terms-checking robot that enforces a very specific type of style enforcement called term-checking. If a specific convention is established for how to notate specific types of information, Rorybot looks for potential violations and corrects them. This standardization for individual types of information, like date/time notation or terminology, will provide clarity and simplicity to the content so readers can focus on the content.

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

### Stage 3
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
