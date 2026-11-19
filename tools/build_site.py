#!/usr/bin/env python3
"""Build the WorkNest SG static career-assist site."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "site"

BRAND = """<svg viewBox="0 0 32 32" aria-hidden="true"><rect width="32" height="32" rx="9" fill="#1f5a4f"/><path d="M6 16.5 16 7l10 9.5" stroke="#f6f3ec" stroke-width="2.4" fill="none" stroke-linecap="round" stroke-linejoin="round"/><path d="M9.5 15v9h13v-9" fill="#f6f3ec"/><circle cx="16" cy="19.5" r="2.4" fill="#c4553a"/></svg>Work<em>Nest</em> SG"""

NAV = [
    ("index.html", "Home", "home"),
    ("career-path.html", "Career path", "path"),
    ("market.html", "Market", "market"),
    ("industries.html", "Industries", "industries"),
    ("applying.html", "Applying", "applying"),
    ("about.html", "About", "about"),
    ("contact.html", "Contact", "contact"),
]

def nav_html(current: str) -> str:
    items = []
    for href, label, key in NAV:
        attr = ' aria-current="page"' if key == current else ""
        items.append(f'<li><a href="{href}"{attr}>{label}</a></li>')
    return "".join(items)


def chrome(title: str, description: str, current: str, main: str) -> str:
    return f"""<!doctype html>
<html lang="en-SG">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="theme-color" content="#1f5a4f">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="css/styles.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap nav">
<a class="brand" href="index.html">{BRAND}</a>
<button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav-list" aria-label="Open menu"><span class="bars"></span></button>
<ul id="nav-list">{nav_html(current)}</ul>
</div></header>
<main id="main">
{main}
</main>
<footer class="site-footer"><div class="wrap">
<div class="foot-grid">
<div><a class="brand" href="index.html">{BRAND}</a>
<p>A career assist path and dated industry briefings for people applying for work in Singapore. General information, not a recruitment service.</p></div>
<div><h2>Path</h2><ul>
<li><a href="career-path.html">Career path</a></li>
<li><a href="market.html">Market update</a></li>
<li><a href="industries.html">Industries</a></li>
<li><a href="skills.html">Skills and training</a></li>
<li><a href="work-options.html">Work options</a></li>
<li><a href="applying.html">Applying</a></li>
</ul></div>
<div><h2>About</h2><ul>
<li><a href="about.html">About</a></li>
<li><a href="updates.html">Update log</a></li>
<li><a href="contact.html">Contact</a></li>
<li><a href="privacy.html">Privacy</a></li>
<li><a href="disclaimer.html">Disclaimer</a></li>
</ul></div>
</div>
<div class="legal">
<p>WorkNest SG is an independent information site. We are not the Ministry of Manpower, the Skills and Workforce Development Agency, CPF Board, or an employment agency. We do not list vacancies or place candidates. Figures describe the national market at the date shown and do not predict the result of any application. Guides are general information, not legal, tax, or financial advice. ScamShield helpline: 1799.</p>
<p>&copy; 2026 WorkNest SG &middot; 22 Orchard Road, #03-01, Singapore 238885 &middot; +65 8396 3756 &middot; support@worknestsg.com</p>
</div>
</div></footer>
<script src="js/main.js"></script>
</body>
</html>
"""


def write(name: str, title: str, description: str, current: str, main: str) -> None:
    (ROOT / name).write_text(chrome(title, description, current, main), encoding="utf-8")


STAMP = """<p class="stamp"><strong>Updated 19 November 2026</strong><span>Next official sector and vacancy release: MOM Labour Market Report 3Q 2026, expected mid-December 2026.</span></p>"""

RAIL = """<aside class="rail">
<h2>While you apply</h2>
<ol>
<li>Read this briefing before you tailor the application.</li>
<li>Compare the ad with the employer's own careers page.</li>
<li>Note hours, workplace, and whether the role is employment or freelance.</li>
<li>Do not pay a fee to be considered.</li>
</ol>
<a class="back" href="career-path.html">Back to the career path</a>
</aside>"""


PAGES = {}

PAGES["index.html"] = (
    "home",
    "Singapore career path and job market briefings | WorkNest SG",
    "A career assist path for job applications in Singapore, with dated briefings on how major industries are hiring now.",
    f"""
<section class="hero"><div class="wrap hero-grid">
<div>
<p class="eyebrow">Career assist path · Singapore</p>
<h1>Read the market, then prepare the application.</h1>
<p class="lede">Six steps for people applying for work in Singapore, plus a plain briefing on how each major industry is actually moving. The pages share general information and are revised when official labour figures change.</p>
<div class="btn-row"><a class="btn btn-primary" href="career-path.html">Start the career path</a><a class="btn btn-ghost" href="market.html">Read the market update</a></div>
</div>
<aside class="snapshot" aria-label="Latest national figures">
<h2>National snapshot</h2>
<div class="snap"><b>2.0%</b><span>Overall unemployment in September 2026, unchanged from the month before.</span></div>
<div class="snap"><b>+27,700</b><span>Total employment growth in the third quarter of 2026. Most of it was non-resident, in construction and manufacturing.</span></div>
<div class="snap"><b>42.3%</b><span>Share of firms expecting to hire in the next three months, in the September 2026 poll. Up from August, and still described by MOM as selective.</span></div>
<p class="src">Ministry of Manpower, Labour Market Advance Release, third quarter 2026. Reviewed 19 November 2026.</p>
</aside>
</div></section>

<section class="alt"><div class="wrap">
<div class="head"><p class="eyebrow">The path</p><h2>Six steps between a job search and an application.</h2>
<p class="lede">The path is a way to organise the search. It does not submit applications for you, and it does not promise an interview or an offer.</p></div>
<ol class="steps">
<li><span class="n">01</span><div><h3><a href="market.html">See where the market is moving</a></h3><p>Separate resident hiring from total employment, and notice which sectors are adding jobs and which are restructuring.</p></div></li>
<li><span class="n">02</span><div><h3><a href="industries.html">Read the industry you have in mind</a></h3><p>Each briefing says what the latest figures show, what that means for an application, and what to check in an advertisement.</p></div></li>
<li><span class="n">03</span><div><h3><a href="skills.html">Match skills, then look at training</a></h3><p>Start from tasks you have already done. Use public course catalogues and credits before you pay a private provider.</p></div></li>
<li><span class="n">04</span><div><h3><a href="work-options.html">Choose an arrangement that fits the week</a></h3><p>Full-time, part-time, contract, hybrid, and freelance work are not the same kind of engagement. Pay, CPF, and hours follow from that difference.</p></div></li>
<li><span class="n">05</span><div><h3><a href="applying.html">Prepare the application and check the listing</a></h3><p>A short, specific application, sent through a channel you can verify, with a stop list for requests that do not belong in hiring.</p></div></li>
<li><span class="n">06</span><div><h3><a href="updates.html">Update the plan when the figures move</a></h3><p>Industry pages carry a review date. The next fuller sector report is expected in mid-December 2026.</p></div></li>
</ol>
</div></section>

<section><div class="wrap">
<div class="head"><p class="eyebrow">Industries</p><h2>The same market, six different situations.</h2>
<p>Labels describe the latest official picture, not a ranking of where you should work. Open a briefing before you rewrite a CV around that industry.</p></div>
<div class="cards">
<a class="card" href="industry-care.html"><span class="pill steady">Steady</span><h3>Care and community</h3><p>Health and social services remain one of the sectors supporting resident employment.</p><span class="more">Read the briefing</span></a>
<a class="card" href="industry-technology.html"><span class="pill cautious">Cautious</span><h3>Technology</h3><p>Vacancies fell by June, retrenchments rose, and resident hiring was subdued in the third quarter.</p><span class="more">Read the briefing</span></a>
<a class="card" href="industry-finance.html"><span class="pill cautious">Cautious</span><h3>Finance</h3><p>Fewer vacancies, more restructuring, and selective hiring rather than a broad pickup.</p><span class="more">Read the briefing</span></a>
<a class="card" href="industry-professional.html"><span class="pill mixed">Mixed</span><h3>Professional services</h3><p>Second-quarter gains cooled. Entry-level professional openings were still part of the June vacancy pool.</p><span class="more">Read the briefing</span></a>
<a class="card" href="industry-logistics.html"><span class="pill mixed">Mixed</span><h3>Logistics and industry</h3><p>Transport and storage supported resident jobs. Manufacturing's headline growth was mostly non-resident.</p><span class="more">Read the briefing</span></a>
<a class="card" href="industry-public.html"><span class="pill steady">Steady</span><h3>Public and essential services</h3><p>Public administration, education, and essential services carried much of the resident employment growth.</p><span class="more">Read the briefing</span></a>
</div>
</div></section>

<section class="alt"><div class="wrap split">
<div>
<p class="eyebrow">How the briefings stay current</p>
<h2>General sharing, with a date on it.</h2>
</div>
<div>
<p>Each industry page is a briefing, not a job board. It summarises what the Ministry of Manpower has published, says what an applicant can reasonably take from that, and names the source.</p>
<p>When a new labour market report is released, the affected pages and the <a href="updates.html">update log</a> change together. Until the third-quarter report arrives, vacancy counts on this site are still the June 2026 figures.</p>
<p><a href="about.html">How we write and what we do not do</a></p>
</div>
</div></section>
""",
)

PAGES["career-path.html"] = (
    "path",
    "Career assist path for job applications in Singapore | WorkNest SG",
    "Six steps to read Singapore's job market, compare an industry, and prepare an application. General information only.",
    f"""
<div class="page-head"><div class="wrap">
<p class="eyebrow">Career path</p>
<h1>A path for the application, not a placement service.</h1>
<p class="lede">Use the steps in order if you are starting out, or jump to the one you are stuck on. Nothing here submits an application or contacts an employer for you.</p>
</div></div>
<section><div class="wrap brief">
<article class="article">
{STAMP}
<h2>01. See where the market is moving</h2>
<p>A rising employment total can be mostly work-permit hiring in construction and manufacturing, while the resident market in technology or finance is quiet. Read the <a href="market.html">national update</a> first so a headline does not send you into a crowded search.</p>
<p>Write down two things: the kind of work you can start within your current notice period, and the hours you can actually give. The market page will not choose for you. It stops you treating every sector as if it were on the same cycle.</p>
<h2>02. Read one industry briefing</h2>
<p>Open the <a href="industries.html">industry list</a> and read the sector you are considering, plus one adjacent sector. Skills such as scheduling, customer communication, records, and basic data work show up in more than one place. The briefing tells you whether resident hiring there is steady, mixed, or cautious right now.</p>
<h2>03. Match skills before you buy training</h2>
<p>List tasks you have done, not only job titles. Compare that list with two or three current advertisements in the sector. Gaps that appear in several ads are worth a course. A gap that appears once is not a reason to enrol. The <a href="skills.html">skills and training</a> page covers SkillsFuture Credit, public catalogues, and questions to ask before you pay.</p>
<h2>04. Decide the arrangement</h2>
<p>An advertisement that says "flexible" can mean hybrid days, shift work, or freelance delivery. Those have different CPF, leave, and tax consequences. Use <a href="work-options.html">work options</a> to name the arrangement you want, then check whether the advertisement is actually offering it.</p>
<h2>05. Apply through a channel you can verify</h2>
<p>The <a href="applying.html">applying</a> page covers how to read an advertisement, what to put in a short application, and the requests that are a reason to stop: upfront fees, Singpass or one-time passwords, and contact that exists only in a messaging app.</p>
<h2>06. Keep a record, then revisit the date</h2>
<p>Note where you applied, the arrangement offered, and the date. When the next labour report lands, reread the industry page rather than assuming last quarter's picture still holds. The <a href="updates.html">update log</a> shows what changed on this site and why.</p>
<div class="callout"><p>If you want in-person career or skills advice, Connect by SWDA at the Lifelong Learning Institute is a public service centre. WorkNest SG is not part of that service and cannot book it for you.</p></div>
</article>
<aside class="rail">
<h2>On this path</h2>
<ol>
<li><a href="market.html">Market update</a></li>
<li><a href="industries.html">Industries</a></li>
<li><a href="skills.html">Skills and training</a></li>
<li><a href="work-options.html">Work options</a></li>
<li><a href="applying.html">Applying</a></li>
<li><a href="updates.html">Update log</a></li>
</ol>
</aside>
</div></section>
""",
)

PAGES["market.html"] = (
    "market",
    "Singapore job market update, November 2026 | WorkNest SG",
    "A plain reading of MOM's third-quarter 2026 advance release and the second-quarter labour market report, for people planning an application.",
    f"""
<div class="page-head"><div class="wrap">
<p class="eyebrow">Market update</p>
<h1>The job market is growing, and it is uneven.</h1>
<p class="lede">Total employment rose again in the third quarter of 2026. Resident hiring was concentrated in essential and public services. Outward-looking sectors were quieter, and retrenchments stayed elevated there.</p>
</div></div>
<section><div class="wrap brief">
<article class="article">
{STAMP}
<div class="takeaways"><h2>What to take from this</h2><ul>
<li>Do not read total employment growth as resident job growth.</li>
<li>Care, transport and storage, and public services are where resident employment is still being supported.</li>
<li>Technology, finance, and professional services had subdued resident growth in the third quarter.</li>
<li>Vacancy counts below are from June 2026. Newer vacancy figures are not out yet.</li>
</ul></div>
<div class="statrow">
<div class="stat"><b>3.0%</b><span>Resident unemployment in September 2026, from 2.9% in August. Citizen unemployment was 3.1%.</span></div>
<div class="stat"><b>4,800</b><span>Retrenchments in the third quarter, 2.0 per 1,000 employees. The count rose; the rate did not.</span></div>
<div class="stat"><b>1.48</b><span>Job vacancies for each unemployed person in June 2026. Vacancies numbered 68,600.</span></div>
</div>
<h2>Employment</h2>
<p>Total employment, excluding migrant domestic workers, grew by 27,700 in the third quarter of 2026. That was faster than the 11,400 increase in the second quarter and the 25,100 increase a year earlier. Both resident and non-resident employment grew faster than in the previous quarter.</p>
<p>Resident employment growth was mainly in public administration and education, transportation and storage, and health and social services. Resident growth in information and communications, financial services, and professional services was subdued. Non-resident employment made up most of the total increase, mainly in construction and manufacturing.</p>
<h2>Unemployment and retrenchment</h2>
<p>Overall unemployment stayed at 2.0% in September 2026. Resident and citizen rates edged up. In the June quarter, the resident long-term unemployment rate was 1.0%, from 0.9% in March. The advance release does not update that long-term rate.</p>
<p>Retrenchments increased from 4,620 in the second quarter to 4,800 in the third. MOM said they remained elevated in selected outward-oriented sectors, and that business reorganisation was still the main reason. In the second quarter, the increases were concentrated in manufacturing (670 to 870), information and communications (530 to 720), and financial services (560 to 710). Reorganisation or restructuring accounted for 72.1% of second-quarter retrenchments.</p>
<p>Among residents retrenched in the second quarter, 54.9% were back in employment within six months, down from 60.7% in the first quarter. The twelve-month re-entry rate was 69.8%. A lower six-month rate means a search can take longer even when unemployment looks low. It is not a forecast for any one person.</p>
<h2>Vacancies, as of June</h2>
<p>Job vacancies fell from 73,300 in March 2026 to 68,600 in June, and from 76,200 in June 2025. The vacancy rate was 2.8%. The largest declines were in financial services (5,800 to 4,500) and information and communications (5,300 to 4,400).</p>
<p>Entry-level PMET vacancies were 31,700 in June, 45.3% of all vacancies. MOM describes these as professional, manager, executive, and technician vacancies advertised with a minimum salary between $2,300 and $5,000, and notes that they spanned sectors such as health and social services and professional services. That range is a statistical definition, not a recommended wage.</p>
<h2>What employers said they might do next</h2>
<p>In September 2026, 42.3% of firms expected to hire in the next three months, up from 30.5% in August. The share expecting to raise wages rose from 16.9% to 19.9%. The share expecting to retrench rose from 2.8% to 3.1%. MOM said hiring and wage expectations improved in September but stayed below July's levels, and that firms remained selective.</p>
<div class="callout"><p>The third-quarter Labour Market Report, expected in mid-December 2026, will add sector employment splits, vacancy counts, turnover, and re-entry rates. Until then, treat vacancy numbers on this site as June figures.</p></div>
<h2>Sources</h2>
<ul class="sources">
<li><a href="https://www.mom.gov.sg/newsroom/press-releases/2026/1030-labour-market-advance-release-3q-2026" rel="noopener">MOM: Labour Market Advance Release, third quarter 2026 (30 October 2026)</a></li>
<li><a href="https://www.mom.gov.sg/newsroom/press-releases/2026/0921-labour-market-report---second-quarter-2026" rel="noopener">MOM: Labour Market Report, second quarter 2026 (21 September 2026)</a></li>
<li><a href="https://stats.mom.gov.sg/iMAS_PdfLibrary/mrsd-Labour-Market-Report-2Q-2026.pdf" rel="noopener">MOM Manpower Research and Statistics Department, Labour Market Report 2Q 2026 (PDF)</a></li>
</ul>
<p><a href="industries.html">Continue to the industry briefings</a></p>
</article>
{RAIL}
</div></section>
""",
)

# Industry bodies follow a shared shape.
INDUSTRIES = [
    (
        "industry-care.html",
        "Care and community health jobs in Singapore | WorkNest SG",
        "How health and social services hiring looks in late 2026, and what to check before you apply.",
        "steady",
        "Steady resident demand",
        "Care and community",
        "Health and social services are still part of the resident hiring story.",
        """
<p>In the third quarter of 2026, resident employment growth was mainly supported by public administration and education, transportation and storage, and health and social services. Care sits in that last group: hospitals, clinics, eldercare, disability support, and community services.</p>
<p>The second-quarter report did not list health and social services among the sectors driving the rise in retrenchments. Those increases were concentrated in manufacturing, information and communications, and financial services. In June, entry-level PMET vacancies spanned sectors that included health and social services. MOM defines that group as vacancies with a minimum salary between $2,300 and $5,000.</p>
<p>A sector that is still adding resident jobs is not an easy sector. Nursing, therapy, pharmacy, and social work have registration or qualification rules. Support and administrative roles often turn on shifts, language, and whether you can work a particular site.</p>
""",
        """
<p>Read the advertisement for the workplace, the shift pattern, and whether the role is employment or a contract for service. Part-time care work under a contract of service is still employment. CPF rules for citizen and permanent-resident employees apply above $50 a month. Confirm the current rule with CPF Board rather than with a recruiter in a chat app.</p>
<p>If the role needs professional registration, check the regulator's own site for what "registered" or "enrolled" means before you pay for a course that claims to qualify you.</p>
<p>Applications that lead with reliable shift attendance, documentation, and working with families tend to match how these roles are described. A generic technology CV does not substitute for that, and a care CV does not need to pretend otherwise.</p>
""",
        ["Registration or enrolment status, if the role is regulated.", "Shift pattern, including nights and weekends, and how far ahead the roster is published.", "Whether the contract is employment or freelance, and who pays CPF.", "Site location and travel time. Community roles are often spread across several centres."],
    ),
    (
        "industry-technology.html",
        "Technology jobs in Singapore: late 2026 market | WorkNest SG",
        "Information and communications hiring is selective. Vacancies fell by June and resident employment growth was subdued in the third quarter.",
        "cautious",
        "Selective, with restructuring",
        "Technology",
        "Information and communications is still hiring, on tighter terms.",
        """
<p>Resident employment growth in information and communications was subdued in the third quarter of 2026, alongside financial services and professional services. That is a change in tone from the second quarter, when the sector still recorded resident employment gains.</p>
<p>Vacancies in the sector fell from 5,300 in March 2026 to 4,400 in June. Retrenchments rose from 530 in the first quarter to 720 in the second. MOM linked higher recruitment and resignation rates in the sector with business restructuring and people moving between firms, not with a broad hiring boom.</p>
<p>Advertisements still ask for data, cloud, cyber, and applied AI work. The useful distinction in an application is whether you have used a tool inside a real workflow, or whether you are listing the tool's name. Employers who are restructuring tend to ask for the first.</p>
""",
        """
<p>Expect fewer open roles than a year ago and more competition for the ones that remain. A short application that names systems, the size of the workload, and what changed because of your work is easier to read than a list of platforms.</p>
<p>Remote and contract arrangements exist in this sector. They are terms in a specific advertisement, not a feature of the industry. Ask which days are in an office, which hours overlap with the team, and whether the engagement is employment.</p>
<p>SWDA announced a public catalogue of more than 200 AI-related courses on 16 September 2026, with a time-limited tool subscription for eligible citizens who enrol and attend. A course from that catalogue is practice time. It is not an offer of work. Check current eligibility on SWDA's own pages.</p>
""",
        ["Which product or system you worked on, and what you were accountable for.", "Whether the role is permanent, contract, or a vendor placement, and who the employer is.", "Office days, time zone overlap, and on-call expectations.", "Any request to pay for equipment, a starter kit, or a training seat in order to be hired."],
    ),
    (
        "industry-finance.html",
        "Finance jobs in Singapore: late 2026 market | WorkNest SG",
        "Financial services vacancies fell by June 2026 and resident hiring was subdued in the third quarter. A briefing for applicants.",
        "cautious",
        "Fewer vacancies, more restructuring",
        "Finance",
        "Financial services is hiring selectively, not broadly.",
        """
<p>Financial services vacancies fell from 5,800 in March 2026 to 4,500 in June, one of the two largest sector declines in that quarter. Retrenchments in the sector rose from 560 in the first quarter to 710 in the second. Business reorganisation was the main reason for retrenchments across the economy.</p>
<p>In the third quarter, resident employment growth in financial services was subdued. The second quarter had still shown resident gains. If you are coming from a 2025 picture of the sector, update it: the advertisements that remain are being filled more carefully, and some teams are smaller than they were.</p>
<p>Roles that keep appearing in public descriptions of the sector include operations, compliance, risk, finance change, and client servicing. That is a description of the work, not a claim that those roles are easy to get.</p>
""",
        """
<p>Name the regulations, products, or processes you have actually handled. "Familiar with compliance" is weaker than a sentence about the control you ran and how often. If you are moving from another sector, map the transferable task: reconciliations, case handling, vendor checks, or management information.</p>
<p>Hybrid working is common in advertisements. Confirm the number of office days and whether they are fixed. A role that says "flexible" and then requires every day in the office is a scheduling fact, not a small print detail.</p>
<p>Licensing applies to some client-facing and representative roles. Check the Monetary Authority of Singapore's public registers yourself if an advertisement says a licence is required or will be sponsored.</p>
""",
        ["The employer of record, especially if a posting comes through an agency.", "Licence or certification requirements, and who pays for them.", "Office days and the latest time you must be reachable.", "Whether pay is base salary, allowance, or commission, and what the commission depends on."],
    ),
    (
        "industry-professional.html",
        "Professional services jobs in Singapore: late 2026 | WorkNest SG",
        "Consulting, accounting, legal, and engineering services: resident hiring cooled in the third quarter after earlier gains.",
        "mixed",
        "Cooled after earlier gains",
        "Professional services",
        "The second-quarter pickup did not carry straight into the third.",
        """
<p>Professional services recorded resident employment gains in the second quarter of 2026, along with other outward-oriented sectors. In the third quarter, resident growth in the sector was subdued. Read both sentences together. A CV strategy built only on the earlier quarter will overstate how many seats are opening.</p>
<p>In June, entry-level PMET vacancies spanned sectors including professional services as well as health and social services. Those 31,700 vacancies were roles advertised with a minimum salary between $2,300 and $5,000. They are a pool for newer applicants, not a promise that every firm is hiring graduates.</p>
<p>The sector covers different businesses: legal, accounting, management consulting, architecture, and engineering. A slowdown in one practice does not describe the others. Look at advertisements in the specific practice, not at the sector label alone.</p>
""",
        """
<p>Professional-services applications are often won or lost on evidence of client work: a memo, a model, a drawing set, a managed account. Describe the deliverable and your part in it. Titles such as "associate" mean different things in different firms.</p>
<p>Project-based contracts are common. Ask the length, whether the contract can end early, and whether you are an employee of the firm or of a staffing company. Those are different pay and CPF situations.</p>
<p>If you are changing career into this sector, the <a href="skills.html">skills page</a> covers how to compare a SkillsFuture course with the tasks in current ads before you enrol.</p>
""",
        ["Employee of the firm, or employed by an agency and deployed to the firm.", "Utilisation or billing expectations, if the advertisement mentions them.", "Qualification route for regulated work, such as accounting or engineering, confirmed with the professional body.", "Whether the project end date is the employment end date."],
    ),
    (
        "industry-logistics.html",
        "Logistics, transport, and manufacturing jobs in Singapore | WorkNest SG",
        "Transport and storage supported resident employment in late 2026. Manufacturing growth was mostly non-resident, alongside higher retrenchments.",
        "mixed",
        "Split between resident transport jobs and industrial hiring",
        "Logistics and industry",
        "Add the transport story and the factory story separately.",
        """
<p>Transportation and storage was one of the sectors supporting resident employment growth in the third quarter of 2026, together with public administration, education, and health and social services. That includes land transport, warehousing, and parts of the supply chain, not every job with "logistics" in the title.</p>
<p>Manufacturing is a different picture. Non-resident employment drove most of the economy's employment increase in the third quarter, mainly in construction and manufacturing. In the second quarter, manufacturing retrenchments rose from 670 to 870. Construction's employment growth is largely work-permit hiring. A large total-employment number there is not a count of resident vacancies.</p>
<p>June vacancy figures for these sectors will be refreshed in the mid-December report. Until then, use the employment and retrenchment split above rather than an older vacancy chart.</p>
""",
        """
<p>Advertisements in transport and warehousing often turn on licence class, shift, and site. Name the licence you hold and the shifts you can work. Do not imply a licence you plan to get later.</p>
<p>In manufacturing, separate production-operator roles from technician and engineer roles. Retrenchment has been higher in this sector than in care or public services, so ask whether the role replaces a leaver or sits in a new line, and how long the contract runs.</p>
<p>Safety orientation and site access rules are part of the job, not an extra. If someone asks you to pay for a "site pass" before any employer has confirmed the role in writing, stop and check the employer's own channel.</p>
""",
        ["Licence or certificate named in the ad, and whether you already hold it.", "Shift hours, overtime practice, and the work site.", "Employment versus a daily-rated or freelance arrangement.", "Who issues any pass or permit, and whether you are being asked to pay for it."],
    ),
    (
        "industry-public.html",
        "Public service and essential services jobs in Singapore | WorkNest SG",
        "Public administration, education, and essential services supported resident employment growth in the third quarter of 2026.",
        "steady",
        "Supporting resident employment",
        "Public and essential services",
        "This is where much of the resident employment growth sat in the third quarter.",
        """
<p>MOM's third-quarter advance release said resident employment growth continued to be supported mainly by essential and public services, naming public administration and education, transportation and storage, and health and social services. This briefing covers the public-administration and education part. Care and transport have their own pages because the day-to-day work is different.</p>
<p>Hiring here often follows budget cycles, schemes, and fixed application windows rather than a rolling private-sector advertisement. A quiet week on a job portal is not the same signal as a quiet week in a private firm.</p>
<p>Second-quarter retrenchment increases were not concentrated in public administration and education. That is a statement about the published figures, not a promise of job security in a particular agency.</p>
""",
        """
<p>Read the scheme details on the agency's own site or on Careers@Gov, not only on a repost. Note citizenship requirements, medical or security checks, and whether the closing date is firm.</p>
<p>Education roles can require a qualification, a registration, or both. Early-childhood and school roles are not interchangeable. Check the relevant agency's eligibility page before you pay for a certificate a private site says is "recognised".</p>
<p>If you are mid-career, look at whether the scheme values occupational experience or asks you to restart on a trainee pay point. Both exist. The advertisement should say which one it is.</p>
""",
        ["Closing date, and whether late applications are accepted.", "Citizenship or residency conditions.", "Checks that take time: registration, medical, or security clearance.", "Pay point for mid-career entrants, if the scheme publishes one."],
    ),
]


def industry_page(slug, title, description, pill, pill_label, h_label, lede, situation, applying, checks):
    items = "".join(f"<li>{c}</li>" for c in checks)
    return f"""
<div class="page-head"><div class="wrap">
<p class="eyebrow">Industry briefing · {h_label}</p>
<h1>{lede}</h1>
<p class="lede"><span class="pill {pill}">{pill_label}</span></p>
</div></div>
<section><div class="wrap brief">
<article class="article">
{STAMP}
<h2>The situation</h2>
{situation}
<h2>If you are applying</h2>
{applying}
<h2>What to check in the advertisement</h2>
<ul class="checks">{items}</ul>
<p class="src-note">National figures: MOM Labour Market Advance Release, third quarter 2026, and Labour Market Report, second quarter 2026. This page is general information. It is not a list of vacancies and it does not rank employers.</p>
<p><a href="industries.html">All industry briefings</a> · <a href="applying.html">How to apply</a></p>
</article>
{RAIL}
</div></section>
"""


PAGES["industries.html"] = (
    "industries",
    "Industry job market briefings for Singapore | WorkNest SG",
    "Dated briefings on care, technology, finance, professional services, logistics, and public services for people applying for work in Singapore.",
    """
<div class="page-head"><div class="wrap">
<p class="eyebrow">Industries</p>
<h1>Six briefings on the current market.</h1>
<p class="lede">Each page is general information about that industry's hiring situation, written for someone preparing an application. They are not job listings.</p>
</div></div>
<section><div class="wrap">
<p class="stamp"><strong>Updated 19 November 2026</strong><span>Vacancy counts are from June 2026 until the third-quarter report is published.</span></p>
<div class="cards">
<a class="card" href="industry-care.html"><span class="pill steady">Steady</span><h3>Care and community</h3><p>Resident employment in health and social services is still being supported. Registration and shifts decide many applications.</p><span class="more">Read the briefing</span></a>
<a class="card" href="industry-technology.html"><span class="pill cautious">Cautious</span><h3>Technology</h3><p>Vacancies down by June, retrenchments up, resident growth subdued in the third quarter.</p><span class="more">Read the briefing</span></a>
<a class="card" href="industry-finance.html"><span class="pill cautious">Cautious</span><h3>Finance</h3><p>Vacancies fell from 5,800 to 4,500 by June. Hiring is selective and restructuring is still in the figures.</p><span class="more">Read the briefing</span></a>
<a class="card" href="industry-professional.html"><span class="pill mixed">Mixed</span><h3>Professional services</h3><p>Second-quarter resident gains cooled. Entry-level professional openings were still in the June pool.</p><span class="more">Read the briefing</span></a>
<a class="card" href="industry-logistics.html"><span class="pill mixed">Mixed</span><h3>Logistics and industry</h3><p>Transport and storage supported resident jobs. Manufacturing and construction growth was mostly non-resident.</p><span class="more">Read the briefing</span></a>
<a class="card" href="industry-public.html"><span class="pill steady">Steady</span><h3>Public and essential services</h3><p>Public administration and education helped carry resident employment growth in the third quarter.</p><span class="more">Read the briefing</span></a>
</div>
<p style="margin-top:1.4rem"><a href="market.html">Read the national update behind these labels</a></p>
</div></section>
""",
)

PAGES["skills.html"] = (
    "none",
    "Skills and training for job applications in Singapore | WorkNest SG",
    "How to compare SkillsFuture Credit, public courses, and career-transition programmes before you pay, using the current job market as the filter.",
    f"""
<div class="page-head"><div class="wrap">
<p class="eyebrow">Skills and training</p>
<h1>Train for a gap you can see in current ads.</h1>
<p class="lede">Start from the industry briefing and two or three advertisements. A course is worth considering when the same missing skill shows up more than once. A course is not a job offer.</p>
</div></div>
<section><div class="wrap brief">
<article class="article">
{STAMP}
<h2>Use the market as the filter</h2>
<p>In a cautious sector such as technology or finance, employers are hiring fewer people and asking for evidence of work already done. A new certificate helps most when the advertisements ask for that skill and your examples are thin. In care and essential services, the filter is often a registration, a language, or a shift pattern, not another general digital badge.</p>
<h2>SkillsFuture Credit</h2>
<p>Singapore citizens aged 25 and above have an opening SkillsFuture Credit of $500. It can be used on courses listed on the MySkillsFuture portal and does not expire. Citizens aged 40 and above also have a mid-career credit of $4,000 for selected courses, which does not expire. From 1 December 2026, new course runs of full Workforce Skills Qualifications and selected sector-agency courses join the mid-career list. Balances and course eligibility are on MySkillsFuture after a Singpass login. Check them there before you pay a provider who says they can "claim it for you".</p>
<h2>Where to look first</h2>
<ul>
<li><a href="https://www.myskillsfuture.gov.sg/" rel="noopener">MySkillsFuture</a> for courses, credit, and subsidies.</li>
<li><a href="https://www.swda.gov.sg/" rel="noopener">Skills and Workforce Development Agency (SWDA)</a>, the statutory board formed from SkillsFuture Singapore and Workforce Singapore, in operation from 1 July 2026.</li>
<li>Connect by SWDA at the Lifelong Learning Institute, for in-person career and skills advice.</li>
<li><a href="https://www.mycareersfuture.gov.sg/" rel="noopener">MyCareersFuture</a>, the government career portal, which also flags some roles tied to public career schemes.</li>
</ul>
<p>SkillsFuture Career Transition Programmes are train-and-place programmes aimed at sectors with hiring opportunities. Places, sectors, and outcomes change. Completing a programme is not the same as receiving an offer. Read the current programme page, including what "place" means and what happens if a match is not made.</p>
<h2>Before you pay anyone</h2>
<ul class="checks">
<li>Is the same course, or a close one, listed on MySkillsFuture?</li>
<li>What can you do at the end that an advertisement in your sector currently asks for?</li>
<li>Who awards the certificate, and is a regulator involved?</li>
<li>Are you being asked for Singpass, a one-time password, or an upfront "registration fee" to unlock a government credit? Stop if you are. Credits are claimed through the official portal.</li>
</ul>
<p class="src-note">Credit amounts and the 1 December 2026 mid-career course change are from SkillsFuture Credit guidance on MySkillsFuture. Confirm your own balance. This page is not training advice for your circumstances.</p>
</article>
<aside class="rail">
<h2>Pair this with</h2>
<ul>
<li><a href="industries.html">Your industry briefing</a></li>
<li><a href="applying.html">The application itself</a></li>
<li><a href="career-path.html">The full path</a></li>
</ul>
</aside>
</div></section>
""",
)

PAGES["work-options.html"] = (
    "none",
    "Work options in Singapore: hours, CPF, and flexible work | WorkNest SG",
    "How part-time, contract, hybrid, remote, and freelance arrangements differ in Singapore, and what to confirm before you accept.",
    f"""
<div class="page-head"><div class="wrap">
<p class="eyebrow">Work options</p>
<h1>Name the arrangement before you compare the pay.</h1>
<p class="lede">Full-time, part-time, contract, hybrid, and freelance work answer different needs. The market briefings tell you where hiring is steadier. This page tells you what the arrangement itself commits you to.</p>
</div></div>
<section><div class="wrap">
{STAMP}
<div class="tablewrap"><table>
<thead><tr><th>Arrangement</th><th>What it usually means</th><th>What to confirm</th></tr></thead>
<tbody>
<tr><td>Full-time employee</td><td>A contract of service, commonly around a standard work week.</td><td>Hours, overtime, leave, probation, and notice.</td></tr>
<tr><td>Part-time employee</td><td>Under the Employment Act, a part-time employee is contracted to work less than 35 hours a week.</td><td>The weekly hours in the contract, how extra hours are paid, and pro-rated leave. You are still an employee.</td></tr>
<tr><td>Fixed-term contract</td><td>Employment that ends on a date or when a project ends.</td><td>Whether it renews, notice during the term, and who the employer is.</td></tr>
<tr><td>Hybrid or work from home</td><td>An arrangement about place, not a separate legal category. Formal flexible-work requests have a process from 1 December 2024.</td><td>Which days, which hours, equipment, and whether the pattern is contractual or informal.</td></tr>
<tr><td>Shift work</td><td>Common in care, transport, security, and food services.</td><td>The roster, rest time, and how far ahead shifts are published.</td></tr>
<tr><td>Freelance or contract for service</td><td>You are paid for a deliverable. This is not employment.</td><td>Payment timing, who owns the work, insurance, and your own CPF and tax position. IRAS and CPF Board publish the distinctions.</td></tr>
</tbody>
</table></div>
<div class="brief">
<article class="article">
<h2>CPF follows employment, including part-time</h2>
<p>If you are a Singapore citizen or permanent resident employed under a contract of service and your total wages are more than $50 a month, your employer must pay CPF. That includes part-time, temporary, and contract employees. If you earn more than $50 and not more than $500 in a month, there is no employee share; the employer still pays the employer share. Contributions are due by the 14th of the following month, or the next working day if the 14th is a weekend or public holiday. Rates change, including an increase for senior employees from 1 January 2027. Check the current table with CPF Board.</p>
<p>Freelance income is treated differently. Do not let an advertisement blur the two by calling you a "partner" when the working arrangement is employment, or the reverse.</p>
<h2>Asking for flexible work</h2>
<p>The Tripartite Guidelines on Flexible Work Arrangement Requests took effect on 1 December 2024. An employee can make a formal request in writing, stating the date, the type of arrangement, the reason, and the start and end if there is one. The employer has up to two months to respond. The guidelines set out a process. They do not require the employer to agree to the request. Informal arrangements can continue without this process.</p>
<p>If you are still applying, ask what arrangement the advertisement is actually offering. A formal request is a step for someone already employed.</p>
<h2>A second stream of income</h2>
<p>Some people add part-time or freelance work beside a main job because hours allow it. Check the existing contract for outside-work clauses, and check rest-time rules, before you assume both can run together. Pay from a second stream is not guaranteed and depends on the hours you can sustain. This site does not estimate earnings.</p>
<p class="src-note">Sources: MOM Employment Act guidance on part-time employment; MOM Tripartite Guidelines on Flexible Work Arrangement Requests; CPF Board, saving as an employee.</p>
</article>
<aside class="rail">
<h2>Use with</h2>
<ul>
<li><a href="industries.html">Industry briefings</a></li>
<li><a href="applying.html">Applying</a></li>
<li><a href="market.html">Market update</a></li>
</ul>
</aside>
</div>
</div></section>
""",
)

PAGES["applying.html"] = (
    "applying",
    "How to apply for a job in Singapore | WorkNest SG",
    "How to read an advertisement, write a short application, and spot requests that do not belong in a genuine hiring process.",
    f"""
<div class="page-head"><div class="wrap">
<p class="eyebrow">Applying</p>
<h1>Send a specific application through a channel you can check.</h1>
<p class="lede">WorkNest SG does not receive CVs and does not forward them. You apply to the employer, or through a public portal such as MyCareersFuture.</p>
</div></div>
<section><div class="wrap brief">
<article class="article">
{STAMP}
<h2>Before you write</h2>
<ol>
<li>Read the <a href="industries.html">industry briefing</a> so the application matches the current situation. A technology application written as if hiring were wide open will sound out of date.</li>
<li>Pick two advertisements you would actually accept, including the hours and the workplace.</li>
<li>List three tasks you have done that match duties in those advertisements. Use the tasks, not only the old job title.</li>
</ol>
<h2>What to put in</h2>
<p>Keep it to a page unless the employer asks for more. Open with the role you are applying for. Then give the three tasks, each with a scale: how often, for whom, and what changed. Close with the arrangement you can work: days, hours, and start date. Leave out a photograph unless the employer asks for one. Leave out NRIC, passport, bank details, and date of birth.</p>
<h2>Where to send it</h2>
<p>Prefer the employer's own careers page. MyCareersFuture, run by SWDA with GovTech, is free to browse without Singpass. Applying there requires Singpass and is for citizens and permanent residents. A repost on another board can be useful as a pointer. It is not, by itself, confirmation that the role exists. If you cannot find the role on the employer's site or on MyCareersFuture, ask the employer through a published company address before you invest more time.</p>
<h2>Read the advertisement for these</h2>
<ul class="checks">
<li>Legal name of the employer, not only a brand or a room in a messaging app.</li>
<li>Employment or freelance, hours, workplace, and pay basis: salary, hourly, or per project.</li>
<li>Closing date, if any, and the documents they actually ask for.</li>
<li>Any cost to you. A genuine employer does not charge you to apply, to interview, or to "release" an offer.</li>
</ul>
<h2>Stop, and check, if you are asked for</h2>
<ul>
<li>Payment, a starter kit you must buy, or a cheque you must bank and partly return.</li>
<li>Singpass login, a one-time password, or your NRIC photo at the first conversation.</li>
<li>Bank details before a written offer from an employer you have verified.</li>
<li>An interview that happens only inside a personal messaging app, with no company email or published phone number.</li>
</ul>
<p>The ScamShield helpline is 1799. If you have lost money, report it to the Police. ACRA's business-profile search is one way to see whether a company name exists. A real registration does not make an offer genuine, and a missing registration is a reason to pause.</p>
<h2>After you send it</h2>
<p>Keep a simple log: employer, role, date, arrangement offered, and where you found it. Most applications do not produce an interview. That is ordinary, especially in sectors where MOM has described hiring as selective. Change the application when the advertisements are asking for something you have not shown. Do not pay a third party who promises interviews.</p>
<div class="callout"><p>Nothing on this page is legal advice. Employment Act, CPF, and flexible-work details should be confirmed with MOM, CPF Board, or TAFEP when a real offer is in front of you.</p></div>
</article>
<aside class="rail">
<h2>Then</h2>
<ul>
<li><a href="work-options.html">Check the arrangement</a></li>
<li><a href="skills.html">Only then consider a course</a></li>
<li><a href="updates.html">See when we last revised the figures</a></li>
</ul>
</aside>
</div></section>
""",
)

PAGES["updates.html"] = (
    "none",
    "Update log | WorkNest SG",
    "What changed in WorkNest SG's Singapore job-market briefings, and which official release the change follows.",
    """
<div class="page-head"><div class="wrap">
<p class="eyebrow">Update log</p>
<h1>What we revised, and why.</h1>
<p class="lede">Industry pages move when an official labour release changes the picture. Older pages stay dated so you can see what they were based on.</p>
</div></div>
<section><div class="wrap article">
<ul class="log">
<li><time datetime="2026-11-19">19 November 2026</time>
<p>Published the career assist path and the first set of industry briefings. National employment, unemployment, retrenchment, and hiring intentions follow MOM's Labour Market Advance Release for the third quarter of 2026, released on 30 October 2026. Vacancy counts, the entry-level PMET definition, second-quarter retrenchment by sector, and the six-month re-entry rate follow the Labour Market Report for the second quarter of 2026, released on 21 September 2026.</p>
<p>SkillsFuture Credit amounts, the 1 December 2026 mid-career course change, SWDA's start on 1 July 2026, and the Tripartite flexible-work guidelines are taken from those agencies' public pages and will be rechecked when those pages change.</p>
<p>Waiting on the Labour Market Report for the third quarter of 2026, which MOM said would be released in mid-December 2026. That report is expected to refresh sector splits, vacancies, turnover, and re-entry. Vacancy figures on this site stay labelled as June 2026 until then.</p>
</li>
</ul>
<p><a href="market.html">Read the current national update</a></p>
</div></section>
""",
)

PAGES["about.html"] = (
    "about",
    "About WorkNest SG",
    "WorkNest SG publishes a career assist path and dated industry briefings for people applying for work in Singapore.",
    """
<div class="page-head"><div class="wrap">
<p class="eyebrow">About</p>
<h1>General information, written so it can be updated.</h1>
<p class="lede">WorkNest SG is for people in Singapore who are preparing a job application and want the current industry picture in plain language.</p>
</div></div>
<section><div class="wrap split">
<div>
<h2>What this is</h2>
<p>The career path is a sequence: read the market, read one industry, compare skills and training, name the work arrangement, then apply through a channel you can check. The industry pages are briefings. They share what official statistics say and what an applicant can reasonably watch for.</p>
<p>We are independent. We are not the Ministry of Manpower, the Skills and Workforce Development Agency, CPF Board, TAFEP, or any employer. We do not list vacancies, recruit, screen, or place candidates.</p>
<h2>How a page gets revised</h2>
<p>A figure stays only while its source is the latest one we have checked. The review date is on the page. The <a href="updates.html">update log</a> says which release triggered the change. If you see a number that the next MOM report has replaced, <a href="contact.html">tell us</a>.</p>
</div>
<div>
<h2>What we will not do</h2>
<ul>
<li>Promise a job, an interview, or a level of pay.</li>
<li>Describe ourselves as a partner or representative of a government agency.</li>
<li>Ask you to send a CV, NRIC, Singpass details, or money.</li>
<li>Estimate how much you could earn.</li>
</ul>
<h2>Find us</h2>
<p>22 Orchard Road, #03-01, Singapore 238885<br>+65 8396 3756<br>support@worknestsg.com</p>
<p><a class="btn btn-primary" href="career-path.html">Start the career path</a></p>
</div>
</div></section>
""",
)

PAGES["contact.html"] = (
    "contact",
    "Contact WorkNest SG",
    "Send a correction or a topic suggestion. WorkNest SG does not take job applications.",
    """
<div class="page-head"><div class="wrap">
<p class="eyebrow">Contact</p>
<h1>Corrections and topic ideas.</h1>
<p class="lede">Tell us if a figure has been superseded, or if a sector is missing. This inbox does not accept job applications and we cannot forward a CV.</p>
</div></div>
<section><div class="wrap split">
<div>
<p>The form opens an email in your own mail app, addressed to support@worknestsg.com. Nothing is stored on this website. Please do not include NRIC numbers, Singpass details, bank information, or attachments you would not want in an ordinary email.</p>
<p>Phone: +65 8396 3756<br>22 Orchard Road, #03-01, Singapore 238885</p>
</div>
<div>
<form id="contact-form" class="form" novalidate>
<div class="field"><label for="name">Name</label><input id="name" name="name" autocomplete="name" required><div class="err" aria-live="polite"></div></div>
<div class="field"><label for="email">Email</label><input id="email" name="email" type="email" autocomplete="email" required><div class="err" aria-live="polite"></div></div>
<div class="field"><label for="topic">Topic</label><select id="topic" name="topic"><option>Correction to a figure</option><option>Industry to cover next</option><option>Question about the career path</option><option>Something else</option></select></div>
<div class="field"><label for="msg">Message</label><textarea id="msg" name="msg" required></textarea><div class="err" aria-live="polite"></div></div>
<button class="btn btn-primary" type="submit">Open email</button>
</form>
<div id="form-ok" class="ok" hidden tabindex="-1">
<h2>Your email app should be open.</h2>
<p>The message is ready for you to send. If nothing opened, write to support@worknestsg.com.</p>
</div>
</div>
</div></section>
""",
)

PAGES["disclaimer.html"] = (
    "about",
    "Disclaimer | WorkNest SG",
    "WorkNest SG publishes general information about Singapore's job market and job applications. No employment or income is promised.",
    """
<div class="page-head"><div class="wrap">
<p class="eyebrow">Disclaimer</p>
<h1>Disclaimer</h1>
</div></div>
<section><div class="wrap article">
<h2>Information only</h2>
<p>WorkNest SG publishes general information about Singapore's labour market, industries, training options, work arrangements, and job applications. We are not an employment agency. We do not publish vacancies and we do not recruit, screen, place, or introduce candidates.</p>
<h2>No outcome is promised</h2>
<p>Nothing on this site promises an interview, a job, or any level of income. Hiring, pay, hours, and contract type differ by employer and change over time. National statistics describe the market at the date cited. They do not predict the result of an application.</p>
<h2>Not professional advice</h2>
<p>Content is not legal, financial, tax, or employment advice. Rules on the Employment Act, CPF, flexible work, and training credits change. Confirm details with the Ministry of Manpower, CPF Board, IRAS, or the Skills and Workforce Development Agency, or with a qualified adviser.</p>
<h2>Sources and third parties</h2>
<p>We name the public source behind figures and link to official sites. We do not control those sites and we are not responsible for their content. We are not affiliated with them.</p>
<h2>Accuracy</h2>
<p>We date each briefing and keep an <a href="updates.html">update log</a>. A page can still lag a release. If you spot an error, <a href="contact.html">write to us</a>.</p>
</div></section>
""",
)

PAGES["privacy.html"] = (
    "about",
    "Privacy Policy | WorkNest SG",
    "How WorkNest SG handles personal data under Singapore's Personal Data Protection Act 2012.",
    """
<div class="page-head"><div class="wrap">
<p class="eyebrow">Privacy</p>
<h1>Privacy Policy</h1>
<p class="lede">Last updated: 19 November 2026</p>
</div></div>
<section><div class="wrap article">
<p>WorkNest SG ("we", "us") handles personal data in line with Singapore's Personal Data Protection Act 2012 (PDPA). This policy explains what happens when you use this website.</p>
<h2>1. Who we are</h2>
<p>WorkNest SG is an independent information website. We publish a career path and industry briefings. We are not an employment agency and we do not collect CVs for placement.</p>
<h2>2. Personal data we collect</h2>
<p>The contact form does not send data to our server. It opens an email in your own mail application. If you email us, we receive what you choose to include, typically your name, email address, and message. Do not send NRIC numbers, Singpass details, one-time passwords, bank details, or passwords. We will not ask for them.</p>
<h2>3. Technical data</h2>
<p>A web host may keep standard server logs, such as IP address, browser type, and pages requested, to keep the site secure and running. This site does not set advertising cookies and does not load third-party fonts or trackers.</p>
<h2>4. How we use personal data</h2>
<ul>
<li>To read and reply to corrections, questions, and topic suggestions.</li>
<li>To keep the website secure.</li>
<li>To meet a legal requirement.</li>
</ul>
<p>We do not sell personal data and we do not use it for a mailing list unless you have agreed to that separately.</p>
<h2>5. Disclosure</h2>
<p>We disclose personal data to a service provider who hosts email only as needed to receive and answer messages, where the law requires it, or with your consent.</p>
<h2>6. Transfers</h2>
<p>If a provider stores mail outside Singapore, we take reasonable steps to see that the data has protection comparable to the PDPA.</p>
<h2>7. Protection and retention</h2>
<p>We take reasonable steps to protect personal data we hold. Email is not perfectly secure. We keep messages only as long as needed to handle the enquiry or as the law requires, then delete or anonymise them.</p>
<h2>8. Your rights</h2>
<p>You may ask for access to personal data we hold about you, ask for a correction, or withdraw consent. Email the Data Protection Officer. We may need to verify your identity. If you withdraw consent, we may not be able to continue the enquiry.</p>
<h2>9. Other websites</h2>
<p>Links to MOM, SWDA, CPF Board, MyCareersFuture, and others leave this site. Their privacy practices are their own.</p>
<h2>10. Children</h2>
<p>This site is a general audience site and is not directed at children. Contact us if you believe a child has sent us personal data and we will delete it.</p>
<h2>11. Changes</h2>
<p>The current policy is this page, with the date above.</p>
<h2>12. Contact</h2>
<ul>
<li>Data Protection Officer, WorkNest SG</li>
<li>support@worknestsg.com</li>
<li>+65 8396 3756</li>
<li>22 Orchard Road, #03-01, Singapore 238885</li>
</ul>
<p>If you are not satisfied with our response, you may contact the Personal Data Protection Commission at <a href="https://www.pdpc.gov.sg" rel="noopener">pdpc.gov.sg</a>.</p>
</div></section>
""",
)


def main() -> None:
    ROOT.mkdir(parents=True, exist_ok=True)
    for name, (current, title, description, body) in PAGES.items():
        # Industry pages set current to industries via filename later
        if name.startswith("industry-"):
            current = "industries"
        write(name, title, description, current, body)
    for row in INDUSTRIES:
        slug, title, description, pill, pill_label, h_label, lede, situation, applying, checks = row
        body = industry_page(slug, title, description, pill, pill_label, h_label, lede, situation, applying, checks)
        write(slug, title, description, "industries", body)
    favicon = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="9" fill="#1f5a4f"/><path d="M6 16.5 16 7l10 9.5" stroke="#f6f3ec" stroke-width="2.4" fill="none" stroke-linecap="round"/><path d="M9.5 15v9h13v-9" fill="#f6f3ec"/><circle cx="16" cy="19.5" r="2.4" fill="#c4553a"/></svg>"""
    (ROOT / "favicon.svg").write_text(favicon, encoding="utf-8")
    print(f"Wrote site to {ROOT}")


if __name__ == "__main__":
    main()
