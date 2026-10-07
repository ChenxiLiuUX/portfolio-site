import os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
def shell(title, body, current="work", desc=""):
    nav = [("Work","index.html#work","work"),("About","index.html#about","about"),("Download resume","resume.pdf","resume")]
    links = "".join(f'<a href="{h}"{" aria-current=\"page\"" if k==current else ""}>{n}</a>' for n,h,k in nav)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Plus+Jakarta+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap">
  {'' if current is None else '<a class="site-name" href="index.html">Chenxi Liu</a>'}
  <nav class="site-nav" aria-label="Main">{links}</nav>
</div></header>

<main id="main" class="wrap">
{body}
</main>

<footer class="site-footer"><div class="wrap"><div class="site-footer__inner"><span>Chenxi Liu, Seattle</span><span class="footer-links"><a href="mailto:chaserliu1994@gmail.com">Email</a><a href="https://www.linkedin.com/in/chenxi-liu-ux" target="_blank" rel="noopener">LinkedIn</a></span></div></div></footer>
</body>
</html>
'''

def T(s): return f'<span class="todo">{s}</span>'

def page_title(name, lead, label=""):
    lab = f'<p class="t-label page-title__label">{label}</p>' if label else ""
    ld = f'<p class="t-lead">{lead}</p>' if lead else ""
    return f'''<div class="page-title">
  <a class="back" href="index.html#work">All work</a>
  {lab}<h1>{name}</h1>
  {ld}
</div>'''

def summary(role, team, timeline, status, problem, outcome, team_label="Team"):
    role = "Lead product designer"
    return f'''<dl class="summary">
  <div><dt>Role</dt><dd>{role}</dd></div>
  <div><dt>{team_label}</dt><dd>{team}</dd></div>
  <div><dt>Timeline</dt><dd>{timeline}</dd></div>
  <div class="summary__wide"><dt>Problem</dt><dd>{problem}</dd></div>
  <div class="summary__wide"><dt>Outcome</dt><dd>{outcome}</dd></div>
</dl>'''

def fig(label, caption, short=False, src=None, w=None, h=None, narrow=False):
    if src:
        return f'''<figure><img class="media-img{' media-img--narrow' if narrow else ''}" src="{src}" alt="{label}" width="{w}" height="{h}" loading="lazy"><figcaption>{caption}</figcaption></figure>'''
    return f'''<figure><div class="media{' media--short' if short else ''}" role="img" aria-label="{label}"></div><figcaption>{caption}</figcaption></figure>'''

def section(id_, heading, paras, extra=""):
    ps = "".join(f"<p>{p}</p>" for p in paras)
    return f'''<section class="section" aria-labelledby="{id_}">
  <div class="split"><h2 id="{id_}">{heading}</h2><div>{ps}</div></div>
  {extra}
</section>'''

def rows(items):
    out = '<div class="rows">'
    for title, parts in items:
        inner = "".join((f'<p class="t-label">{k}</p>' if not v else f'<p>{"<span class=\"row__k\">"+k+"</span>" if k else ""}{v}</p>') for k, v in parts)
        out += f'<div class="row"><h3>{title}</h3><div>{inner}</div></div>'
    return out + '</div>'

def pains(items):
    out = '<div class="rows">'
    for title, text, src in items:
        out += f'<div class="row"><h3>{title}</h3><p>{text}<span class="row__src">{src}</span></p></div>'
    return out + '</div>'

def metrics(items, four=False):
    out = f'<div class="metrics{" metrics--4" if four else ""}">'
    for num, text, cap in items:
        empty = num == "—"
        out += f'<div class="metric"><span class="metric__num{" metric__num--empty" if empty else ""}">{num}</span><p>{text}</p><span class="t-caption">{cap}</span></div>'
    return out + '</div>'

def results(intro, items, what="this project", reflection=None):
    return f'''<section class="section" aria-labelledby="results">
  <div class="split"><h2 id="results">Results and what's next</h2><div><p>{intro}</p></div></div>
  {metrics(items)}
  <div class="split mt-8"><h2>Looking back</h2><div><p>{reflection or T(f"Two or three sentences: what you'd do differently, and what {what} taught you.")}</p></div></div>
</section>'''

def nxt(href, name):
    return f'''<div class="next">
  <a href="index.html#work"><span class="t-label">Back</span><span class="next__title">All work</span></a>
  <a href="{href}"><span class="t-label">Next project</span><span class="next__title">{name}</span></a>
</div>'''

pending = lambda s: f'<span class="tag tag--pending">{s}</span>'
tag = lambda s: f'<span class="tag">{s}</span>'

# ================= HOME =================
COVERS = {
    "case-parallel-chatbot.html": ("images/cover-chatbot.jpg", "The chatbot entry panel: a word cloud of common struggles, a free-text input, and a book-a-call link"),
    "case-shopify-audits.html": ("images/cover-audits.jpg", "My recommended concern-first navigation for Peace Out: Shop by concern as the primary menu, with category and featured as secondary, and ingredient as a filter"),
    "case-parallel-admin.html": ("images/cover-admin.jpg", "The redesigned admin overview: weekly metrics, a meeting-mix chart, and client status cards that flag what needs attention"),
}

def card(href, name, sub, text, role="Lead product designer"):
    cover = COVERS.get(href)
    media = (f'<div class="card__media"><img src="{cover[0]}" alt="{cover[1]}" width="1600" height="1200" loading="lazy"></div>'
             if cover else f'<div class="card__media" role="img" aria-label="{name} preview"></div>')
    return f'''<article class="card">
    {media}
    <div class="card__body"><h3>{name}</h3><p class="card__sub">{sub}</p><p class="card__role">{role}</p><p>{text}</p><a class="button card__cta" href="{href}">Read case study<span class="visually-hidden">: {name}</span> <span aria-hidden="true">→</span></a></div>
  </article>'''

home = f'''<div class="hero">
  <h1>Chenxi Liu</h1>
  <p class="hero__statement">UX designer who turns complex systems into products that feel intuitive, with the rigor of years spent in scientific research. Based in Seattle.</p>
</div>

<section id="work" aria-labelledby="work-h">
<h2 id="work-h" class="section-title">Work</h2>
<div class="card-list">
  {card("case-parallel-chatbot.html","Years of Consultant Expertise Made Interactive","Parallel e-commerce agency, 2026","I designed and shipped an AI chatbot that carries the agency founder's expertise to every website visitor, then redesigned it to serve e-commerce brands arriving with different needs.")}
  {card("case-parallel-admin.html","Designing an Internal Operating System","Parallel e-commerce agency, 2026","I designed an internal operating system for an e-commerce agency, streamlining how the team runs meetings, tracks work, and reports to clients.")}
  {card("case-shopify-audits.html","Two Beauty Brands, Two Different UX Strategies","Parallel e-commerce agency, 2026","I advised two beauty brands, Peace Out and Winky Lux, on the user experience of their Shopify sites, with 34 findings focused on earning shoppers&rsquo; trust and improving conversion.")}
  {card("case-maya-migrate.html","Maya Migrate","Nonprofit legal tech, 2026","I designed a free case-management app for immigrants and the lawyers who serve them, from the design system to App Store release, including an emergency check-in feature for people at risk of detention.")}
</div>
</section>

<section class="section" id="impact" aria-labelledby="impact-h">
  <div class="split"><h2 id="impact-h">Impact</h2><div><p class="t-muted">Every figure here has a source you can ask me about.</p></div></div>
  {metrics([("Live","Shipped to the App Store as the sole designer, from design system to release.","Maya Migrate, 2026"),("6","Frictions found in a moderated study of a live AI chatbot, each answered in the approved redesign.","Parallel, 2026"),("34","Findings across two Shopify audits, each rated by severity and effort.","Peace Out, Winky Lux"),("60 → 25","Product tiles to real choices on one category page, without dropping a SKU.","Winky Lux recommendation")], four=True)}
</section>

<section class="section" id="about" aria-labelledby="about-h">
  <div class="about">
    <div class="about__side">
      <h2 id="about-h">About</h2>
      <img class="about__photo" src="images/chenxi-liu.jpg" alt="Chenxi Liu, smiling, in a cap and glasses" width="800" height="1000">
    </div>
    <div class="about__body">
      <p>I spent years running experiments before I started designing. The habit stuck: I treat every design as a hypothesis, test it with real people, and write down what I learned.</p>
      <p>Today I design AI tools, internal systems, and e-commerce experiences, and I'm most at home where a product has to make something complicated feel simple.</p>
      <div class="button-row">
        <a class="button button--on-dark" href="resume.pdf" download>Download resume</a>
        <a class="button button--secondary button--on-dark" href="https://www.linkedin.com/in/chenxi-liu-ux" target="_blank" rel="noopener">LinkedIn</a>
      </div>
    </div>
  </div>
</section>'''
open('index.html','w').write(shell("Chenxi Liu — Product designer", home, current=None, desc="Chenxi Liu is a UX designer in Seattle with a background in scientific research."))

# ================= CHATBOT =================
def quotes(items):
    return '<div class="quotes">' + "".join(f'<blockquote class="pull-quote"><p>{q}</p><footer>{w}</footer></blockquote>' for q, w in items) + '</div>'

chat = page_title("Years of Consultant Expertise Made Interactive", "", "Parallel e-commerce agency, 2026") + summary(
  "Lead UX designer, v1 and v2", "Agency founder, one engineer", "2026", tag("v1 studied")+" "+pending("v2 awaiting build"),
  "The chatbot is Parallel's front door: the first place a prospective client meets the founder's thinking, and the main path to a booked call. The live version asked a chain of screening questions before offering anything useful, so visitors expecting expertise got an intake form instead.",
  "I designed and shipped v1, studied it with three target users, and turned six ranked frictions into an approved v2 that answers every one.") + \
  fig("The v2 homepage hero: the agency headline on the left and the chatbot entry on the right, with a word cloud of struggles and a book-a-call link","The v2 entry. The chatbot moves out of a floating widget and into the homepage hero, where visitors start from their own problem.", src="images/chatbot-hero.jpg", w=1427, h=753) + \
  section("context","Context",["Parallel is a boutique e-commerce strategy agency for CPG and beauty brands. Its chatbot sits on the agency's website and is trained on the founder's voice and expertise, so visitors can get a taste of his thinking before they book a call.","For a boutique agency, that matters: the founder can only take so many calls, so the chatbot has to carry his expertise to every visitor and send the right ones to his calendar.","I designed the first version as a single flow. A button opened a chat that asked a series of lead-qualifying questions and ended at a booking calendar. Once it was live, I set out to test my own design with real users and fix whatever wasn't working."]) + \
  section("research","Testing the live chatbot",["I ran moderated walkthroughs of the live chatbot with three people who match Parallel's audience: a current client who founded a brand, an agency CEO, and a former marketplace lead. A follow-up survey covered both the technical execution and the conversation itself.","The execution held up well, so those parts stayed in the redesign."],
    metrics([("3/3","Noticed the chat button right away.","Visibility"),("3/3","Found the responses easy to understand.","Clarity"),("3/3","Moved through the booking calendar smoothly.","Booking"),("3/3","Confirmed the AI sounded like the founder.","Voice")], four=True)) + \
  section("core-finding","The core finding",["The problem was structural. A single, rigid flow front-loaded screening questions before delivering any value, and each participant described the same frustration in their own words."],
    quotes([("It promised his expertise but delivered an intake form that interrogates.","Participant, current client"),("It's a receptionist, not a salesperson.","Participant, agency CEO"),("It's action-oriented but doesn't tell you what Parallel is.","Participant, former marketplace lead")])) + \
  section("findings","Six frictions, ranked",["I ranked every pain point by how many participants raised it and how much it would affect bookings. The redesign had to answer all six."],
    rows([
      ("One flow can't serve different intents",[("3 of 3 participants, high priority","")]),
      ("Too many questions before booking",[("2 of 3, high priority","")]),
      ("It qualifies but doesn't sell Parallel",[("2 of 3, high priority","")]),
      ("No sense of what the chat involves",[("1 of 3, medium priority","")]),
      ("Privacy concerns with no reassurance",[("1 of 3, medium priority","")]),
      ("No social proof",[("1 of 3, medium priority","")])])) + \
  section("decisions","Key decisions",["Seven decisions shaped v2. Each one answers a finding, and most borrow from patterns that already work in e-commerce."],
    rows([
      ("Two doors for two kinds of visitor",[("The situation","v1 assumed everyone arrived with the same goal. In fact, cold visitors needed to build trust first, while warm leads already wanted a call, and one path failed both."),("What I chose","An explore door, where visitors tap a struggle in a word cloud, and an express door that goes straight to booking. Both converge on the same booked call, so there's one outcome to measure."),("Why it works","It's the same logic as browsing versus Buy Now in a store: never make a ready buyer sit through the discovery experience.")]),
      ("Give value before asking for anything",[("The situation","v1 qualified visitors before it showed them why Parallel was worth talking to."),("What I chose","The explore door opens with a tailored insight in the founder's voice. Questions come only after the visitor has received something useful."),("Why it works","Every ask has to be earned. The order of value and ask matters more than the number of questions.")]),
      ("One card instead of a chain of questions",[("The situation","Asking one question at a time felt conversational, but it caused fatigue, and visitors couldn't tell how much more was coming."),("What I chose","The bot frames a short, finite ask and shows every field at once in a single card."),("Why it works","A conversational interface isn't always the right one, even inside a chatbot. Like a checkout progress bar, a visible, bounded request lowers abandonment.")]),
      ("Never ask twice",[("The situation","Explore visitors have already told the bot what they're struggling with by the time they reach the qualifying step."),("What I chose","Their struggle carries over, so their card is shorter than the express version."),("Why it works","Each repeated question adds to the cost of a flow. Carrying context forward is the conversational version of a prefilled checkout.")]),
      ("Reassure at the moment of doubt",[("The situation","Participants wanted proof and privacy reassurance, but sending them to a case-study page would break the flow."),("What I chose","Testimonials appear as a proof layer at moments of hesitation while the chat stays open, and a brief privacy note sits near the input."),("Why it works","It's the same reason reviews sit beside Add to Cart: put the reassurance where the hesitation happens.")]),
      ("Keep the voice that works",[("The situation","All three participants confirmed the bot sounded like the founder. It was the one part of v1 everyone trusted."),("What I chose","v2 builds on that voice and gives it a bigger role, leading the explore door with an insight rather than a question.")]),
      ("Design for the founder too",[("The situation","The founder still needs context before each call, which is why v1 front-loaded a screener."),("What I chose","Every booking sends him a short summary of the visitor's struggle, brand, stage, and contact details, so he walks in prepared without the visitor sitting through a screener.")])])) + \
  section("design","The design",["The chatbot moves out of the floating widget and into the homepage hero, using the site's own type and colors. The headline stays, and the right-hand column becomes the entry. The booking calendar that tested well in v1 is unchanged."],
    fig("v2 user flow: two doors converging on a booked call","Two doors, one destination. Testimonials sit beside the flow as a proof layer rather than a separate path.") +
    fig("Qualifying card with all fields visible","The qualifying card replaces question-after-question with one bounded request.", True) +
    fig("Mobile screens","On mobile, the chat takes over the full screen. On desktop, it stays in a fixed container with the header and footer pinned.", True)) + \
  results("The founder approved the v2 scope, and it's waiting on implementation. Once it's live, I'll re-run the same study and report these measures against v1.",
    [("—","Visitors who start a conversation from the hero.",pending("Awaiting build")),("—","Booked calls from the explore and express doors.",pending("Awaiting build")),("—","Drop-off before booking, compared with v1.",pending("Awaiting build"))],
    reflection="I had treated qualifying visitors as the same thing as converting them. v1 did exactly what I designed it to do, collecting information, and that turned out to be the problem. Now I start with what a visitor needs to get from a flow before deciding what the business needs from them.") + nxt("case-parallel-admin.html","Designing an Internal Operating System")
open('case-parallel-chatbot.html','w').write(shell("Parallel chatbot — Chenxi Liu", chat, desc="Case study: researching and redesigning an AI chatbot for an e-commerce strategy agency."))

# ================= MAYA =================
maya = page_title("Maya Migrate", "A calm, free case-management app for people in a frightening process.", "Nonprofit legal tech, 2026") + summary(
  "Sole product designer", T("Founders, engineers"), T("Year, e.g. 2025–2026"), tag("Live on the App Store"),
  "Immigrants and the solo lawyers who serve them needed a free, trustworthy way to manage cases. The product started as engineer-made mockups, with no design system and a critical safety feature described in technical jargon.",
  "A design system, a redesigned app and landing page, and an emergency check-in feature, designed end to end and now live.") + \
  fig("App dashboard and check-in feature","The mobile dashboard and the check-in feature, in the indigo brand system.") + \
  section("context","Context",["Maya Migrate is an immigrant-led nonprofit. Its platform is free for immigrants and the solo lawyers who represent them, it keeps data collection lean, and it never sells user data. The people using it are often under real stress, so every screen has to feel steady and clear.","I joined as the only designer. My first step was a UX critique of the existing mockups, followed by redesigns of the core screens."],
    pains([("Nothing looked like it belonged together","Screens built directly by engineers had no shared colors, type, or spacing, so the app felt unfinished at the moments people most needed to trust it.","Known going in, from the UX critique"),("The safety feature spoke in jargon","The emergency feature was called a \"dead man's switch\" that users would \"arm,\" language that is confusing at best and alarming for someone worried about detention.","Known going in, from the project scope")])) + \
  section("decisions","Key decisions",["Trauma-informed design was the brief. In practice, that came down to four decisions."], rows([
    ("Plain words for a frightening feature",[("The situation","The feature alerts a person's trusted contacts and lawyer if they stop checking in, which could mean they've been detained."),("What I chose","I renamed it the check-in feature and replaced \"arm\" with \"turn on.\" I kept the copy calm and factual throughout, describing what will happen without dramatizing it.")]),
    ("Make every color mean one thing",[("The situation","In an app about legal risk, a stray red or a warning-colored button can read as an emergency."),("What I chose","Indigo is the primary surface, amber means paused or needs attention, red is reserved for destructive actions only, and green signals status. I checked contrast across the palette and flagged pairings that didn't pass.")]),
    ("Build the system before the screens",[("The situation","As the only designer, I needed every new screen to be fast to make and consistent with the rest."),("What I chose","I set up five color ramps, text styles, a spacing scale, and corner-radius tokens, then later ran a cleanup pass that bound every frame to the shared styles so the file stays maintainable for whoever comes next.")]),
    ("Design the alert as a whole journey",[("The situation","A safety feature fails if any step is unclear: setting it up, living with it, or receiving the alert."),("What I chose","I designed the full path: a setup wizard for desktop and mobile, dashboard states for empty, active, and paused, and five email templates for the people who receive alerts.")])])) + \
  section("design","The design",["Beyond the app itself, I designed the landing page, an animated splash screen in the brand indigo, and a research plan for testing the check-in feature with real users."],
    fig("Check-in setup wizard, desktop and mobile","Setting up the check-in feature, one decision per step.") +
    fig("Dashboard states: empty, active, paused","Amber marks a paused check-in without reading as an emergency.", True) +
    fig("Design system: color ramps and type","Five color ramps, text styles, and spacing tokens, shared across every screen.", True)) + \
  results("The app is live on the App Store. Live user studies of the check-in feature are next, and these are the measures I'll report.",
    [("—","People reached through the app.",tag("Live")),("—","Users who finish setting up a check-in.",tag("Live")),("—","What live studies show about trust and clarity.",pending("Studies planned"))]) + nxt("case-parallel-chatbot.html","Years of Consultant Expertise Made Interactive")
open('case-maya-migrate.html','w').write(shell("Maya Migrate — Chenxi Liu", maya, desc="Case study: a free case-management app for immigrants and their lawyers."))

# ================= ADMIN =================
admin = page_title("Designing an Internal Operating System", "From data collector to decision tool.", "Parallel e-commerce agency, 2026") + summary(
  "Sole UX designer", "Agency founder, shareholders, one engineer", "2026", tag("v3 designed")+" "+pending("v4 in progress"),
  "Parallel's internal tool recorded every meeting and chatbot conversation but surfaced almost none of it. Of 328 recorded calls, about 16 had usable analysis. The team was collecting data it couldn't act on.",
  "A 23-finding review, a phased scope, and a redesign built around how the team works, now evolving to match the agency's own operating procedure.") + \
  fig("The redesigned admin overview: metrics with week-over-week change, a meeting-mix chart, client status cards with Take action buttons, to-do throughput, and this week's meetings with agenda status","The redesigned overview, with weekly client status, workload, and the week's meetings in one place.", src="images/admin-overview.jpg", w=1600, h=1700) + \
  section("context","Context",["Parallel's team runs client, partner, and internal meetings all week. A bot records them, and AI turns each one into a summary, key topics, and to-dos that get pushed to Monday.com. The same tool tracks conversations from the website chatbot and holds the knowledge base the chatbot learns from.","Engineers built the first version quickly, and it captured everything. My work went three levels deep: first the interface, then the team's workflow, and finally the way the agency itself runs."]) + \
  section("interface","The interface: the signal was buried",["I started with a review of the original build across all four screens. On nearly every one, the useful rows were buried under empty ones, so finding the meeting that went sideways or the lead worth calling took far longer than it should."],
    metrics([("16 of 328","Recorded calls with usable AI analysis.","From my review"),("75 of 96","Chatbot conversations that were cold, most of them single-message bounces.","From my review"),("23","Findings ranked by impact: 8 high, 11 medium, and 4 quick wins.","Shared with shareholders")]) +
    pains([("Broken widgets undermined every number","The executive summary read \"No data available\" on a page full of data, and a trend chart looked flat against real volume. Each one quietly signaled that the tool couldn't be trusted.","From my review of the original build"),
           ("The most valuable insight was cut off","The AI's reasoning about how each meeting went, the part that actually helps someone act, was truncated with no way to open it.","From my review of the original build"),
           ("Rows nobody could tell apart","Most meetings had no title, and every chatbot lead was labeled with a machine ID.","From my review of the original build"),
           ("The knowledge base was write-only","Admins could upload files for the chatbot to learn from, but couldn't see what it already knew.","From my review of the original build")])) + \
  section("workflow","The workflow: fit the tool to the work",["A walk-through with the founder changed the question. The team didn't need cleaner tables; they needed a tool that matched how they actually work. Columns like platform and sentiment went unused, while client, meeting type, and owner were missing entirely, and calls the bot couldn't join simply vanished from the record.","I wrote a scope as a pre-read for the shareholders. It ranked the work into what to do now and what to do next on a modest budget, and marked each item that depended on engineering so those questions could be answered early. The shareholders chose to start with meetings, the most-used part of the tool. I then designed in short loops with the founder: build, review, adjust. Four decisions shaped the result."],
    rows([
      ("Give every meeting one home",[("The situation","Meetings showed up in a list, a detail page, the dashboard, and the weekly preview. The same information lived in four places and drifted apart."),("What I chose","Meetings became the system of record, called Checkpoints. The dashboard only reads out and links down. I folded the list, the meeting record, and its agenda into one tab and retired the standalone pages."),("The tradeoff","One denser screen instead of several simpler ones, in exchange for a single source of truth.")]),
      ("Only let people send what they can see",[("The situation","My first design put a \"Send report\" button on each client card in the overview. In review, the founder pointed out that admins couldn't see the full report from there, so they couldn't be sure what they'd be sending."),("What I chose","Cards now link to the full client report, and sending happens only where the whole report is visible, through one shared send screen with a preview of what the client will see.")]),
      ("Show the task, hide the setup",[("The situation","A single meeting could produce anywhere from 5 to more than 40 to-dos, and each one needed six fields to push to Monday.com."),("What I chose","Progressive disclosure. Each to-do is one scannable line with its owner and push status, and the full setup opens only for the task you expand. The bulk action counts what's left (\"Push 2 to Monday\") so its scope is never ambiguous.")]),
      ("Design for what the AI can't do yet",[("The situation","The AI couldn't reliably tell internal meetings from client ones, and the bot couldn't join last-minute calls."),("What I chose","Instead of hiding those gaps, I designed for them: an \"unclassified\" state with quick reclassification and saved rules that train future tagging, and a manual transcript upload for calls the bot missed.")])])) + \
  section("design","The design",["The redesigned tool has four areas: an overview of the week, a sendable report for each client, the Checkpoints record for every meeting, and an admin view of the website chatbot, where I replaced arbitrary lead scores with three signals that are real: conversations, contact info shared, and calls booked.","Before handoff, I mapped every screen and modal in a user-flow diagram and scanned the designs for missing states, so engineering wouldn't hit dead-end buttons."],
    fig("Client report view and send flow","A weekly client report that's ready to send, with a preview of exactly what the client will see.") +
    fig("Checkpoints record with to-dos expanded","One meeting record: details, agenda, summary, to-dos, and transcript, each in its own block.", True) +
    fig("User-flow diagram","The full flow handed to engineering, from screens to modals to confirmation states.", True)) + \
  section("operations","The agency: design for how it runs",["After the redesign, the founders shared their own written procedure for how every meeting should be prepared, run, and followed up. I mapped it onto the designs screen by screen. It did two things."],
    rows([
      ("It confirmed the core",[("What matched","Written independently, the procedure landed on decisions the redesign had already made: no algorithm grading how a client sounds, a person approving everything before it goes out, a sendable report for each client, and the knowledge base as the chatbot's memory.")]),
      ("It raised the bar",[("Speak the agency's language","The team has its own vocabulary for meeting stages, owners, and health, and the tool should use it wherever it maps to a real state."),("Route, don't just display","The overview should tell each person where to start, ranked by urgency, instead of only reporting numbers."),("Recaps that hold people accountable","A generic summary becomes a structured recap: what was decided, who committed to what and by when, and open questions."),("A human gate on everything sent","Reports become drafts that a person reviews and sends, rather than messages the tool sends on its own.")])])) + \
  results("v3 is designed and with engineering, and the next version is being shaped around the agency's procedure. Once the tool is in production, these are the measures I'll report.",
    [("—","Hours saved each week on client reporting.",pending("In build")),("—","To-dos pushed to Monday.com without manual re-entry.",pending("In build")),("—","Meetings with usable analysis, compared with 16 of 328 before.",pending("In build"))],
    reflection="I started by fixing screens. The biggest gains came from learning how the team actually works, first from a walk-through and then from the agency's own procedure. Next time, I'll ask for that procedure on day one.") + nxt("case-shopify-audits.html","Two Beauty Brands, Two Different UX Strategies")
open('case-parallel-admin.html','w').write(shell("Parallel admin tool — Chenxi Liu", admin, desc="Case study: turning an agency's internal tool from a data collector into a decision tool."))

# ================= AUDITS =================
def pair(b_label, b_cap, a_label, a_cap, b_src=None, a_src=None):
    def one(label, cap, src):
        if src:
            return f'<figure><img class="media-img" src="{src}" alt="{label}" width="1600" height="900" loading="lazy"><figcaption>{cap}</figcaption></figure>'
        return f'<figure><div class="media media--short" role="img" aria-label="{label}"></div><figcaption>{cap}</figcaption></figure>'
    return f'<div class="figure-pair">{one(b_label, b_cap, b_src)}{one(a_label, a_cap, a_src)}</div>'

audits = page_title("Two Beauty Brands, Two Different UX Strategies", "Same category, same platform, opposite shoppers.", "Parallel e-commerce agency, 2026") + summary(
  "Sole UX reviewer", "Peace Out Skincare, Winky Lux", "2026", tag("Delivered"),
  "Two beauty brands on Shopify, each with a site that didn't reflect how its customers actually shop. Same category and platform, but opposite shoppers.",
  "34 findings across both sites, each rated by severity and effort, with a prioritized roadmap and redesign direction for each brand.", team_label="Clients") + \
  section("context","Context",["Both audits came through Parallel's work with beauty brands. Peace Out's customers arrive with a skin problem they want solved. Winky Lux's customers arrive for a mood, a flavor, or a small treat.","Running the two back to back made one thing clear: the same method can, and should, produce opposite recommendations. A good audit starts from how a specific customer shops, not from a generic checklist."]) + \
  section("method","Method",["I evaluated each site through four lenses: Nielsen Norman Group's usability heuristics, Baymard Institute's e-commerce research, a task-based walkthrough of the core journey from finding a product to checkout, and WCAG 2.2 AA for accessibility.","Every finding records what's happening, why it matters to the shopper and the business, a recommendation, and evidence. Each is rated by severity and by effort, so the team can sequence the work instead of facing a flat list."],
    metrics([("15","Findings for Peace Out, 9 of them rated major.","Peace Out, July 2026"),("19","Findings for Winky Lux, from site structure to product pages.","Winky Lux, August 2026"),("4","Lenses applied to every finding: heuristics, e-commerce research, task walkthrough, accessibility.","Both audits")])) + \
  section("peaceout","Peace Out: shoppers arrive with a problem",["Peace Out is a direct-to-consumer skincare brand known for acne care. The site had real strengths: high-volume reviews, clinical-study framing, press validation, and concern-based entry points on the homepage. The problems were in structure, hierarchy, and trust."],
    rows([
      ("Three ways to browse one catalog",[("What I found","The header browsed by ingredient, the homepage and filters by concern, and the footer by use case. Shoppers had to re-orient at every level, and no single model was reinforced."),("What I recommended","Commit to concern as the primary model, since it matches how shoppers describe themselves. Ingredient becomes a filter, promotions move under Shop, and the top navigation shrinks to three items: Shop, Learn, and Refer.")]),
      ("Headings that shout at every level",[("What I found","One condensed, all-caps display face stood in for six or seven levels of hierarchy, so weight stopped signaling structure. In one section, an ingredient name was set larger than the header it belonged to."),("What I recommended","A three-to-four-level type scale where no child outranks its parent, with sentence case for product names and sub-headers.")]),
      ("Product information trapped in images",[("What I found","Much of the product page's gallery was text on images: benefits, ingredients, and how-to steps, often repeating the copy beside them."),("What I recommended","Move essential text into live HTML. It's a clutter fix and an accessibility fix at once, since screen readers and search can't read text in images.")]),
      ("Mixed signals at the moment of purchase",[("What I found","The banner promised free shipping sitewide while the cart showed a progress bar toward a free-shipping threshold. Review counts for the flagship product differed between pages, and two different products showed the identical count."),("What I recommended","Reconcile the shipping policy with the interface, and source review counts from one system of record so every surface matches.")])]) +
    pair("Peace Out's current header navigation, mixing shop, bestsellers, sale, shop by ingredient, rewards, and learn","Before. Ingredient in the header, concern on the homepage, use case in the footer.","My recommended concern-first navigation, with shop by concern as the primary menu","After. One concern-first model, with ingredient and skin type as filters.", b_src="images/audits-nav-before.jpg", a_src="images/audits-nav-after.jpg") +
    fig("My recommended product page structure: a clear title and price, a simple buy box, then description, how to use, key ingredients, details, and reviews as live text","A restructured product page with a clear type scale, live text in place of image text, and one benefits statement.", src="images/audits-pdp.jpg", w=1206, h=2048, narrow=True)) + \
  section("winky","Winky Lux: shoppers arrive for a mood",["Winky Lux is a color-cosmetics brand that is loud, playful, and built on small, affordable treats, with new flavors and seasonal drops almost every month. The site's problem was a gap: the brand's personality and the way it merchandises showed up at the edges of the site, but not where people actually shop."],
    rows([
      ("Navigation by body part, merchandising by collection",[("What I found","The navigation was organized as Lip, Eye, and Face, while the brand sells through collections, flavors, and finishes. A shopper looking for a mood had to already know the product's name. The header and footer also used two different category schemes."),("What I recommended","Add a collections tier alongside categories, with landing pages that carry each collection's story, and align the footer to the same structure.")]),
      ("One product, many tiles",[("What I found","The lip page was a flat grid of about 60 tiles, with the same product appearing as a single, a mini, a trio, and a set."),("What I recommended","Make the product family the grid unit (\"8 flavors, from $18\"), move size and pack count onto the product page as variants, and give sets their own surface. That takes the page from about 60 tiles to about 25 real choices without dropping a SKU.")]),
      ("Filters that skip the selling points",[("What I found","The only filter was an unlabeled color picker, and it was slow to respond. Finish, flavor, and format, the things that make these products distinct, couldn't be filtered at all."),("What I recommended","Facets for finish, flavor or scent, format, collection, and price, with shade names shown in the color filter.")]),
      ("The differentiator was buried",[("What I found","The brand's color-changing pH technology, its hardest-to-copy feature, sat in a mid-page banner. The first screen sold one product rather than the brand, which matters for shoppers arriving cold from social media."),("What I recommended","Bring the brand line into the hero, and show the color change rather than describe it, using before-and-after imagery or short video.")]),
      ("The brand stopped at the edges of the page",[("What I found","Pattern and saturated color appeared in the announcement bar and footer, while the product grid, filters, and buy buttons were neutral black and white."),("What I recommended","Decide deliberately where color earns its place, in collection headers, category tiles, empty states, and calls to action, and test brand-colored buttons against black with contrast verified.")])]) +
    pair("Current lip page grid with repeated products","Before. The same product repeated across singles, minis, trios, and sets.","Recommended product-family grid","After. "+T("One line on the family-grid mockup, or remove this pair if you don't have one."))) + \
  section("both","What showed up on both sites",["Different brands and different shoppers, but the same three failure points appeared on both."],
    rows([
      ("Contradictory structure",[("",'On both sites, the header and footer organized the catalog in different ways, so neither model became learnable.')]),
      ("Social proof that looked fabricated",[("","Both sites showed identical review counts on different products. Reviews were a genuine strength for both brands, and a visible data error undercuts exactly that.")]),
      ("Flat hierarchy on the product page",[("","Both product pages made it hard to tell titles, sections, and body text apart, which slows scanning at the moment of decision.")])])) + \
  results("Both audits were delivered to the brands' teams through Parallel. I'm following up on which recommendations shipped and what changed, and these are the measures I'll report.",
    [("—","Recommendations implemented.",pending("Following up")),("—","Change in conversion after changes ship.",pending("Following up")),("—","Accessibility issues resolved.",pending("Following up"))],
    reflection="Running two audits back to back taught me that the same heuristics can lead to opposite answers. The method stays fixed, but the recommendation has to come from how that particular customer shops.") + nxt("case-maya-migrate.html","Maya Migrate")
open('case-shopify-audits.html','w').write(shell("Shopify UX audits — Chenxi Liu", audits, desc="Case study: UX audits for two beauty brands with opposite ways of shopping."))
print("pages ok")
