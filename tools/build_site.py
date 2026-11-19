#!/usr/bin/env python3
"""Build the WorkNest SG static career-assist site."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "site"

BRAND = """<svg viewBox="0 0 32 32" aria-hidden="true"><rect width="32" height="32" rx="9" fill="#1f5a4f"/><path d="M6 16.5 16 7l10 9.5" stroke="#f6f3ec" stroke-width="2.4" fill="none" stroke-linecap="round" stroke-linejoin="round"/><path d="M9.5 15v9h13v-9" fill="#f6f3ec"/><circle cx="16" cy="19.5" r="2.4" fill="#c4553a"/></svg>Work<em>Nest</em> SG"""

NAV = [
    ("index.html", "Home", "home"),
    ("work-options.html", "Work types", "work"),
    ("industries.html", "Industries", "industries"),
    ("market.html", "Market", "market"),
    ("applying.html", "Applications", "applying"),
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
<p>A guide to full-time, part-time, hybrid, online, contract, project-based, and freelance work in Singapore, with the current job market alongside.</p></div>
<div><h2>Work types</h2><ul>
<li><a href="work-options.html#full-time">Full-time work</a></li>
<li><a href="work-options.html#part-time">Part-time work</a></li>
<li><a href="work-options.html#hybrid">Hybrid work</a></li>
<li><a href="work-options.html#online">Online work</a></li>
<li><a href="work-options.html#contract">Contract and project work</a></li>
<li><a href="work-options.html#freelance">Freelance work</a></li>
</ul></div>
<div><h2>Market</h2><ul>
<li><a href="industries.html">Industries</a></li>
<li><a href="market.html">National market</a></li>
<li><a href="applying.html">Applications</a></li>
<li><a href="skills.html">Skills and training</a></li>
<li><a href="career-path.html">Overview</a></li>
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
<p>WorkNest SG is an independent guide. It is not the Ministry of Manpower, the Skills and Workforce Development Agency, CPF Board, or an employment agency. It does not list vacancies or place candidates. The figures describe the national market on the date shown, and the pages are general guidance. ScamShield helpline: 1799.</p>
<p>&copy; 2026 WorkNest SG &middot; 22 Orchard Road, #03-01, Singapore 238885 &middot; +65 8396 3756 &middot; support@worknestsg.com</p>
</div>
</div></footer>
<script src="js/main.js"></script>
</body>
</html>
"""


def write(name: str, title: str, description: str, current: str, main: str) -> None:
    (ROOT / name).write_text(chrome(title, description, current, main), encoding="utf-8")


STAMP = """<p class="stamp"><strong>Updated 19 November 2026</strong><span>The next official look at sectors and vacancies is the MOM Labour Market Report for the third quarter of 2026, expected in mid-December 2026.</span></p>"""

RAIL = """<aside class="rail">
<h2>How to read the figures</h2>
<ul>
<li>They describe the country as a whole. One employer can look quite different.</li>
<li>Hours, the workplace, and the type of contract are written in each advertisement.</li>
<li>A fee just to be considered is not part of ordinary hiring.</li>
</ul>
<a class="back" href="market.html">See the national picture</a>
</aside>"""


PAGES = {}

PAGES["index.html"] = (
    "home",
    "Full-time, part-time, hybrid, online, contract and freelance work in Singapore | WorkNest SG",
    "A guide to full-time, part-time, hybrid, online, contract, project-based, and freelance work in Singapore, set against the latest job-market figures.",
    f"""
<section class="hero"><div class="wrap">
<p class="eyebrow">Work types in Singapore · November 2026</p>
<h1><span>Full-time</span>, <span>part-time</span>, <span>hybrid</span>, <span>online</span>, <span>contract</span>, and <span>freelance</span> work.</h1>
<div class="hero-grid">
<div>
<p class="lede">If you are looking at one of these, the market is not the same for each. Full-time and part-time roles are easier to find in care, transport, and public services right now. Hybrid, online, contract, project-based, and freelance work turn up more often in technology, finance, and professional services, where openings are fewer.</p>
<div class="btn-row"><a class="btn btn-primary" href="work-options.html">Work types</a><a class="btn btn-ghost" href="industries.html">By industry</a></div>
</div>
<aside class="snapshot" aria-label="Latest national figures">
<h2>National snapshot</h2>
<div class="snap"><b>2.0%</b><span>Overall unemployment in September 2026, unchanged from the month before.</span></div>
<div class="snap"><b>+27,700</b><span>Total employment growth in the third quarter of 2026. Most of it was non-resident, in construction and manufacturing.</span></div>
<div class="snap"><b>42.3%</b><span>Share of firms expecting to hire in the next three months, in the September 2026 poll. Up from August, and still described by MOM as selective.</span></div>
<p class="src">Ministry of Manpower, Labour Market Advance Release, third quarter 2026. Reviewed 19 November 2026.</p>
</aside>
</div></div></section>

<section class="alt"><div class="wrap">
<div class="head"><p class="eyebrow">The six arrangements</p><h2>Where each kind of work sits this quarter.</h2>
<p class="lede">This follows the latest Ministry of Manpower picture. Pay and hours still depend on the role you are looking at.</p></div>
<div class="cards">
<a class="card" href="work-options.html#full-time"><h3>Full-time work</h3><p>Still the main pattern in public services, care, and transport, where resident hiring is holding up.</p><span class="more">More about this</span></a>
<a class="card" href="work-options.html#part-time"><h3>Part-time work</h3><p>Under 35 hours a week. Common in care, transport, and essential services, and sometimes alongside a full-time job.</p><span class="more">More about this</span></a>
<a class="card" href="work-options.html#hybrid"><h3>Hybrid work</h3><p>Still written into technology and finance advertisements, even though vacancies in those sectors fell.</p><span class="more">More about this</span></a>
<a class="card" href="work-options.html#online"><h3>Online work</h3><p>Shows up in technology, professional services, and some freelance projects. Many postings still include office days.</p><span class="more">More about this</span></a>
<a class="card" href="work-options.html#contract"><h3>Contract and project-based work</h3><p>Common in technology and professional services, often with an end date, while those sectors restructure.</p><span class="more">More about this</span></a>
<a class="card" href="work-options.html#freelance"><h3>Freelance work</h3><p>Paid per project, outside employment. Some people take it beside a main job. CPF and tax follow the self-employed rules.</p><span class="more">More about this</span></a>
</div>
</div></section>

<section><div class="wrap">
<div class="head"><p class="eyebrow">By industry</p><h2>The same kind of work can meet a different market.</h2>
<p>A full-time care role and a hybrid technology role are not competing in the same conditions this quarter.</p></div>
<div class="cards">
<a class="card" href="industry-care.html"><span class="pill steady">Steady</span><h3>Care and community</h3><p>Full-time and part-time shifts. Resident hiring in health and social services is still being supported.</p><span class="more">More about this</span></a>
<a class="card" href="industry-technology.html"><span class="pill cautious">Cautious</span><h3>Technology</h3><p>Hybrid, online, contract, and freelance work remain in advertisements. Vacancies fell, and resident hiring was slower.</p><span class="more">More about this</span></a>
<a class="card" href="industry-finance.html"><span class="pill cautious">Cautious</span><h3>Finance</h3><p>Mostly full-time and hybrid. Vacancies fell from 5,800 to 4,500, and hiring is selective.</p><span class="more">More about this</span></a>
<a class="card" href="industry-professional.html"><span class="pill mixed">Mixed</span><h3>Professional services</h3><p>Project-based contracts, hybrid days, and some freelance work. Earlier resident gains cooled.</p><span class="more">More about this</span></a>
<a class="card" href="industry-logistics.html"><span class="pill mixed">Mixed</span><h3>Logistics and industry</h3><p>Full-time and part-time site work. Transport supported resident jobs. Online work is limited.</p><span class="more">More about this</span></a>
<a class="card" href="industry-public.html"><span class="pill steady">Steady</span><h3>Public and essential services</h3><p>Full-time schemes, with some part-time. This is where much of the resident employment growth sat.</p><span class="more">More about this</span></a>
</div>
</div></section>

<section class="alt"><div class="wrap split">
<div>
<p class="eyebrow">Keeping the guide current</p>
<h2>We update the pages when the official figures change.</h2>
</div>
<div>
<p>Each industry page follows the latest Ministry of Manpower release and says where the numbers come from. When a new labour market report comes out, we update the pages it affects and record that in the <a href="updates.html">update log</a>.</p>
<p>Vacancy counts here are still the June 2026 figures. The third-quarter report is expected in mid-December.</p>
<p><a href="about.html">About this guide</a></p>
</div>
</div></section>
""",
)

PAGES["career-path.html"] = (
    "path",
    "A guide to Singapore's job market | WorkNest SG",
    "A short guide to Singapore's current job market, six industries, training credits, and how work is usually arranged.",
    f"""
<div class="page-head"><div class="wrap">
<p class="eyebrow">Overview</p>
<h1>The market is moving in more than one direction.</h1>
<p class="lede">Full-time and part-time hiring is concentrated in essential and public services. Hybrid, online, contract, project-based, and freelance work are easier to spot in technology, finance, and professional services, where the quarter is quieter. The guide below stays with that split.</p>
</div></div>
<section><div class="wrap brief">
<article class="article">
{STAMP}
<h2>The national picture</h2>
<p>A rising employment total can be mostly work-permit hiring in construction and manufacturing, while resident hiring in technology or finance is quiet. The <a href="market.html">national picture</a> keeps those two measures apart: total employment rose by 27,700 in the third quarter of 2026, and most of that increase was non-resident.</p>
<p>Sectors are also on different cycles. Care, transport and storage, and public services supported resident employment. Information and communications, financial services, and professional services had slower resident growth in the same quarter.</p>
<h2>Industries</h2>
<p>Each <a href="industries.html">industry guide</a> stays with one sector. Scheduling, customer conversations, records, and basic data work show up in more than one of them. The label on each page — steady, mixed, or cautious — follows the latest official release for that sector.</p>
<h2>Skills and training</h2>
<p>Job titles often overlap. A skill that appears in several current advertisements is the kind of thing public course lists are built around. A skill that appears once is more specific to that role. The <a href="skills.html">skills and training guide</a> covers SkillsFuture Credit and the public course list, including the amounts and which courses they apply to.</p>
<h2>Work arrangements</h2>
<p>"Flexible" in an advertisement can mean hybrid days, shift work, or freelance delivery. Those are not the same thing for CPF, leave, or tax. The <a href="work-options.html">work types guide</a> explains how full-time, part-time, hybrid, online, contract, and freelance work are usually set up in Singapore.</p>
<h2>Applications</h2>
<p>An advertisement usually names an employer, the hours, a workplace, and how pay is calculated. Some messages also ask for a fee, a Singpass login, a one-time password, or a chat that exists only in a messaging app. The <a href="applying.html">applications guide</a> covers both what is ordinary and what is worth treating with care.</p>
<h2>Dates on the pages</h2>
<p>Each industry page shows the date it was last checked against an official release. The <a href="updates.html">update log</a> records which release that was. The next fuller sector report is expected in mid-December 2026.</p>
<div class="callout"><p>Connect by SWDA, at the Lifelong Learning Institute, is a public centre where you can talk about careers and skills. This guide is independent of that service.</p></div>
</article>
<aside class="rail">
<h2>In this guide</h2>
<ul>
<li><a href="market.html">National market</a></li>
<li><a href="industries.html">Industries</a></li>
<li><a href="skills.html">Skills and training</a></li>
<li><a href="work-options.html">Work arrangements</a></li>
<li><a href="applying.html">Applications</a></li>
<li><a href="updates.html">Update log</a></li>
</ul>
</aside>
</div></section>
""",
)

PAGES["market.html"] = (
    "market",
    "Singapore job market update, November 2026 | WorkNest SG",
    "Singapore's labour market in late 2026: employment, unemployment, vacancies, and where resident hiring is concentrated.",
    f"""
<div class="page-head"><div class="wrap">
<p class="eyebrow">Market update</p>
<h1>The job market is growing, and it is uneven.</h1>
<p class="lede">Total employment rose again in the third quarter of 2026. Resident hiring was concentrated in essential and public services. Outward-looking sectors were quieter, and retrenchments stayed elevated there.</p>
</div></div>
<section><div class="wrap brief">
<article class="article">
{STAMP}
<div class="takeaways"><h2>The quarter in short</h2><ul>
<li>Total employment and resident hiring are separate measures. Most of the 27,700 increase was non-resident.</li>
<li>Resident employment was supported in care, transport and storage, and public services.</li>
<li>Technology, finance, and professional services had slower resident growth.</li>
<li>The vacancy counts below are from June 2026. Newer vacancy numbers are not out yet.</li>
</ul></div>
<div class="statrow">
<div class="stat"><b>3.0%</b><span>Resident unemployment in September 2026, from 2.9% in August. Citizen unemployment was 3.1%.</span></div>
<div class="stat"><b>4,800</b><span>Retrenchments in the third quarter, 2.0 per 1,000 employees. The count rose; the rate did not.</span></div>
<div class="stat"><b>1.48</b><span>Job vacancies for each unemployed person in June 2026. Vacancies numbered 68,600.</span></div>
</div>
<h2>Employment</h2>
<p>Total employment, excluding migrant domestic workers, grew by 27,700 in the third quarter of 2026. That was faster than the 11,400 increase in the second quarter and the 25,100 increase a year earlier. Both resident and non-resident employment grew faster than in the previous quarter.</p>
<p>Resident employment growth was mainly in public administration and education, transportation and storage, and health and social services. Resident growth in information and communications, financial services, and professional services was slower. Non-resident employment made up most of the total increase, mainly in construction and manufacturing.</p>
<h2>Unemployment and retrenchment</h2>
<p>Overall unemployment stayed at 2.0% in September 2026. Resident and citizen rates edged up. In the June quarter, the resident long-term unemployment rate was 1.0%, from 0.9% in March. The advance release does not update that long-term rate.</p>
<p>Retrenchments increased from 4,620 in the second quarter to 4,800 in the third. MOM said they remained elevated in selected outward-oriented sectors, and that business reorganisation was still the main reason. In the second quarter, the increases were concentrated in manufacturing (670 to 870), information and communications (530 to 720), and financial services (560 to 710). Reorganisation or restructuring accounted for 72.1% of second-quarter retrenchments.</p>
<p>Among residents retrenched in the second quarter, 54.9% were back in employment within six months, down from 60.7% in the first quarter. The twelve-month re-entry rate was 69.8%. People can take longer to find the next role even while the unemployment rate stays low. These are averages for a group. One person's search can be shorter or longer.</p>
<h2>Vacancies, as of June</h2>
<p>Job vacancies fell from 73,300 in March 2026 to 68,600 in June, and from 76,200 in June 2025. The vacancy rate was 2.8%. The largest declines were in financial services (5,800 to 4,500) and information and communications (5,300 to 4,400).</p>
<p>Entry-level PMET vacancies were 31,700 in June, 45.3% of all vacancies. MOM uses this for professional, manager, executive, and technician roles advertised with a minimum salary between $2,300 and $5,000, across sectors such as health and social services and professional services. That band is how the survey defines the group. It is not a recommended wage.</p>
<h2>What employers said they might do next</h2>
<p>In September 2026, 42.3% of firms expected to hire in the next three months, up from 30.5% in August. The share expecting to raise wages rose from 16.9% to 19.9%. The share expecting to retrench rose from 2.8% to 3.1%. MOM said hiring and wage expectations improved in September but stayed below July's levels, and that firms remained selective.</p>
<div class="callout"><p>The third-quarter Labour Market Report, expected in mid-December 2026, should add sector employment splits, vacancy counts, turnover, and re-entry rates. Until then, the vacancy numbers here stay as the June figures.</p></div>
<h2>Sources</h2>
<ul class="sources">
<li><a href="https://www.mom.gov.sg/newsroom/press-releases/2026/1030-labour-market-advance-release-3q-2026" rel="noopener">MOM: Labour Market Advance Release, third quarter 2026 (30 October 2026)</a></li>
<li><a href="https://www.mom.gov.sg/newsroom/press-releases/2026/0921-labour-market-report---second-quarter-2026" rel="noopener">MOM: Labour Market Report, second quarter 2026 (21 September 2026)</a></li>
<li><a href="https://stats.mom.gov.sg/iMAS_PdfLibrary/mrsd-Labour-Market-Report-2Q-2026.pdf" rel="noopener">MOM Manpower Research and Statistics Department, Labour Market Report 2Q 2026 (PDF)</a></li>
</ul>
<p><a href="industries.html">Industry guides</a></p>
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
        "Health and social services in late 2026: resident employment is still being supported, with registration and shifts common in the work.",
        "steady",
        "Steady resident demand",
        "Care and community",
        "Health and social services are still part of the resident hiring story.",
        """
<p>In the third quarter of 2026, resident employment growth was mainly supported by public administration and education, transportation and storage, and health and social services. Care sits in that last group: hospitals, clinics, eldercare, disability support, and community services.</p>
<p>The second-quarter report did not list health and social services among the sectors driving the rise in retrenchments. Those increases were concentrated in manufacturing, information and communications, and financial services. In June, entry-level PMET vacancies spanned sectors that included health and social services. MOM defines that group as vacancies with a minimum salary between $2,300 and $5,000.</p>
<p>Nursing, therapy, pharmacy, and social work carry registration or qualification rules. Support and administrative roles more often turn on shifts, language, and the centre where the work happens.</p>
""",
        """
<p>Advertisements in care usually say where you would work, the shift pattern, and whether the role is employment or freelance. Part-time care work under a contract of service is still employment. For citizens and permanent residents, CPF applies once monthly wages are more than $50. The current table is on the CPF Board site.</p>
<p>If the role is regulated, "registered" or "enrolled" is defined on the regulator's own site. Care advertisements commonly mention shift attendance, records, and work with families.</p>
""",
        ["Whether the role needs registration or enrolment.", "The shift pattern, including nights and weekends, and how far ahead the roster is published.", "Whether you would be an employee or freelance, and who pays CPF.", "Where the work is based. Community roles are often spread across several centres."],
    ),
    (
        "industry-technology.html",
        "Technology jobs in Singapore: late 2026 market | WorkNest SG",
        "Information and communications hiring is selective. Vacancies fell by June and resident employment growth was slower in the third quarter.",
        "cautious",
        "Selective, with restructuring",
        "Technology",
        "Information and communications is still hiring, on tighter terms.",
        """
<p>Resident employment growth in information and communications was slower in the third quarter of 2026, alongside financial services and professional services. That is a change in tone from the second quarter, when the sector still recorded resident employment gains.</p>
<p>Vacancies in the sector fell from 5,300 in March 2026 to 4,400 in June. Retrenchments rose from 530 in the first quarter to 720 in the second. MOM linked higher recruitment and resignation rates in the sector with business restructuring and people moving between firms, not with a broad hiring boom.</p>
<p>You will still see advertisements for data, cloud, cyber, and applied AI work. In a quarter shaped by restructuring, those advertisements tend to describe a tool used in day-to-day work, rather than a list of product names.</p>
""",
        """
<p>There are fewer openings than a year earlier. The advertisements that remain tend to name a system, the size of the workload, and what changed. Some mention remote days or a contract. That is true of that advertisement. Many technology roles are still based in an office.</p>
<p>On 16 September 2026, SWDA published a public list of more than 200 AI-related courses, with a time-limited tool subscription for eligible citizens who enrol and attend. Who can use it is explained on SWDA's own pages. The list is courses, not jobs.</p>
""",
        ["The system you would work on, and which part of the work is yours.", "Whether the role is permanent, a contract, or a placement through a vendor, and who the employer would be.", "Office days, time-zone overlap, and on-call hours.", "Any fee for equipment, a starter kit, or a training seat before you can be considered. Ordinary employers do not charge that."],
    ),
    (
        "industry-finance.html",
        "Finance jobs in Singapore: late 2026 market | WorkNest SG",
        "Financial services in late 2026: fewer vacancies, more restructuring, and slower resident employment growth.",
        "cautious",
        "Fewer vacancies, more restructuring",
        "Finance",
        "Financial services is hiring selectively, not broadly.",
        """
<p>Financial services vacancies fell from 5,800 in March 2026 to 4,500 in June, one of the two largest sector declines in that quarter. Retrenchments in the sector rose from 560 in the first quarter to 710 in the second. Business reorganisation was the main reason for retrenchments across the economy.</p>
<p>In the third quarter, resident employment growth in financial services was slower. The second quarter had still shown resident gains. Against a 2025 picture of the sector, the later figures show fewer vacancies and smaller teams in some areas, with the remaining advertisements filled more selectively.</p>
<p>You will still see advertisements for operations, compliance, risk, finance change, and client servicing. The vacancy count is how many openings there were in June.</p>
""",
        """
<p>Advertisements that are still open often name a regulation, a product, or a process, such as reconciliations, case handling, vendor checks, or management information. Hybrid wording is common, and the number of office days is usually in the same advertisement. A role described as flexible can still mean every day in the office. The advertisement is where that schedule is spelled out.</p>
<p>Some client-facing and representative roles refer to a licence. The Monetary Authority of Singapore keeps public registers for those roles. An advertisement sometimes says whether a licence is required, or whether the employer will sponsor it.</p>
""",
        ["Who the employer is, including when the advertisement comes through an agency.", "Any licence or certification, and who pays for it.", "How many days are in the office, and the hours you would need to be reachable.", "Whether pay is salary, an allowance, or commission, and what the commission depends on."],
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
<p>Professional services recorded resident employment gains in the second quarter of 2026, along with other outward-oriented sectors. In the third quarter, resident growth in the sector was slower. The two quarters together show a cooler market than the second quarter on its own.</p>
<p>In June, entry-level PMET vacancies included professional services and health and social services. Those 31,700 vacancies were roles advertised with a minimum salary between $2,300 and $5,000. That groups many kinds of roles by the salary floor in the advertisement. Individual firms still differ.</p>
<p>The sector covers legal, accounting, management consulting, architecture, and engineering. A slow quarter in one practice can sit next to a steadier one. An advertisement in the practice you are looking at will tell you more than the sector label.</p>
""",
        """
<p>Advertisements here often refer to a piece of client work: a memo, a model, a drawing set, a managed account. Titles such as "associate" mean different things from one firm to another. Project-based contracts are common. The length, whether it can end early, and who employs you — the firm itself, or a staffing company — change the pay and the CPF position.</p>
<p>The <a href="skills.html">skills and training guide</a> explains SkillsFuture Credit and the public course list that sit beside these advertisements.</p>
""",
        ["Whether you would be employed by the firm, or by an agency placed at the firm.", "Any utilisation or billing target, if the advertisement mentions one.", "The qualification path for regulated work such as accounting or engineering, as the professional body describes it.", "Whether the project end date is also the end of the employment."],
    ),
    (
        "industry-logistics.html",
        "Logistics, transport, and manufacturing jobs in Singapore | WorkNest SG",
        "Transport and storage supported resident employment in late 2026. Manufacturing growth was mostly non-resident, alongside higher retrenchments.",
        "mixed",
        "Split between resident transport jobs and industrial hiring",
        "Logistics and industry",
        "Transport supported resident jobs. Manufacturing's growth was mostly non-resident.",
        """
<p>Transportation and storage was one of the sectors supporting resident employment growth in the third quarter of 2026, together with public administration, education, and health and social services. That includes land transport, warehousing, and parts of the supply chain, not every job with "logistics" in the title.</p>
<p>Manufacturing is a different picture. Non-resident employment drove most of the economy's employment increase in the third quarter, mainly in construction and manufacturing. In the second quarter, manufacturing retrenchments rose from 670 to 870. Construction's employment growth is largely work-permit hiring. A large total-employment number there is not a count of resident vacancies.</p>
<p>June vacancy figures for these sectors will be refreshed in the mid-December report. Until then, the employment and retrenchment split above is the later evidence.</p>
""",
        """
<p>In transport and warehousing, advertisements often turn on licence class, shift, and site. In manufacturing, a production-operator role and a technician or engineer role are different advertisements. Retrenchment has been higher here than in care or public services, so the length of a contract is worth reading carefully.</p>
<p>Safety orientation and site access are part of the job. If someone asks you to pay for a "site pass" before a named employer has confirmed the role in writing, that is not how ordinary hiring works. A genuine role also appears on the employer's own website or a known public portal.</p>
""",
        ["The licence or certificate named in the advertisement.", "Shift hours, how overtime usually works, and the work site.", "Whether the role is employment, daily-rated work, or freelance.", "Who issues any pass or permit, and whether a fee is involved."],
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
<p>MOM's third-quarter advance release said resident employment growth continued to be supported mainly by essential and public services: public administration and education, transportation and storage, and health and social services. This page covers public administration and education. Care and transport have their own pages because the day-to-day work is different.</p>
<p>Hiring here often follows budget cycles, schemes, and fixed windows, rather than a rolling private-sector advertisement. A quiet week on a job portal can simply be the gap between those windows.</p>
<p>The rise in retrenchments in the second quarter was concentrated in other sectors. Public administration and education were not among them. One agency can still differ from the sector as a whole.</p>
""",
        """
<p>Scheme details are usually on the agency's own site or on Careers@Gov, as well as on any repost. Citizenship conditions, medical or security checks, and closing dates are commonly part of those pages.</p>
<p>An education role can ask for a qualification, a registration, or both. Early-childhood and school roles are different schemes. The agency's eligibility page explains what a certificate is for. Mid-career schemes sometimes recognise work experience and sometimes use a trainee pay point. The advertisement is where you can see which of those applies.</p>
""",
        ["The closing date, and whether late applications are accepted.", "Any citizenship or residency conditions.", "Registration, a medical check, or security clearance, where the scheme includes them.", "The pay point for mid-career entrants, if the scheme publishes one."],
    ),
]


def industry_page(slug, title, description, pill, pill_label, h_label, lede, situation, applying, checks):
    items = "".join(f"<li>{c}</li>" for c in checks)
    return f"""
<div class="page-head"><div class="wrap">
<p class="eyebrow">Industry guide · {h_label}</p>
<h1>{lede}</h1>
<p class="lede"><span class="pill {pill}">{pill_label}</span></p>
</div></div>
<section><div class="wrap brief">
<article class="article">
{STAMP}
<h2>What the market looks like</h2>
{situation}
<h2>What the advertisements tend to say</h2>
{applying}
<h2>Worth looking for in an advertisement</h2>
<ul class="checks">{items}</ul>
<p class="src-note">National figures come from MOM's Labour Market Advance Release for the third quarter of 2026 and the Labour Market Report for the second quarter of 2026.</p>
<p><a href="industries.html">All industries</a> · <a href="applying.html">Applications</a></p>
</article>
{RAIL}
</div></section>
"""


PAGES["industries.html"] = (
    "industries",
    "Industry guides to Singapore's job market | WorkNest SG",
    "How full-time, part-time, hybrid, online, contract, and freelance work show up in care, technology, finance, and other Singapore sectors.",
    """
<div class="page-head"><div class="wrap">
<p class="eyebrow">Industries</p>
<h1>Where full-time, hybrid, online, and freelance work are showing up.</h1>
<p class="lede">Each guide stays with one sector, and with the arrangements you will usually see advertised there: full-time, part-time, hybrid, online, contract or project-based, and freelance.</p>
</div></div>
<section><div class="wrap">
<p class="stamp"><strong>Updated 19 November 2026</strong><span>Vacancy counts are from June 2026 until the third-quarter report is published.</span></p>
<div class="cards">
<a class="card" href="industry-care.html"><span class="pill steady">Steady</span><h3>Care and community</h3><p>Full-time and part-time shifts. Resident employment in health and social services is still being supported.</p><span class="more">More about this</span></a>
<a class="card" href="industry-technology.html"><span class="pill cautious">Cautious</span><h3>Technology</h3><p>Hybrid, online, contract, and freelance advertisements, with fewer vacancies and slower resident growth.</p><span class="more">More about this</span></a>
<a class="card" href="industry-finance.html"><span class="pill cautious">Cautious</span><h3>Finance</h3><p>Full-time and hybrid work. Vacancies fell from 5,800 to 4,500, and hiring is selective.</p><span class="more">More about this</span></a>
<a class="card" href="industry-professional.html"><span class="pill mixed">Mixed</span><h3>Professional services</h3><p>Project-based contracts, hybrid days, and some freelance work. Earlier resident gains cooled.</p><span class="more">More about this</span></a>
<a class="card" href="industry-logistics.html"><span class="pill mixed">Mixed</span><h3>Logistics and industry</h3><p>Full-time and part-time site work. Transport supported resident jobs. Online work is limited.</p><span class="more">More about this</span></a>
<a class="card" href="industry-public.html"><span class="pill steady">Steady</span><h3>Public and essential services</h3><p>Full-time schemes, with some part-time hours. Resident employment growth was supported here.</p><span class="more">More about this</span></a>
</div>
<p style="margin-top:1.4rem"><a href="market.html">The national picture behind these labels</a></p>
</div></section>
""",
)

PAGES["skills.html"] = (
    "none",
    "Skills and training for job applications in Singapore | WorkNest SG",
    "SkillsFuture Credit, public courses, and how training fits beside a job search in Singapore right now.",
    f"""
<div class="page-head"><div class="wrap">
<p class="eyebrow">Skills and training</p>
<h1>Courses and credits you can look at while you search.</h1>
<p class="lede">In a quarter when some sectors are hiring more carefully, advertisements tend to name a specific skill, a registration, or a shift pattern. Public credits and course lists show what is available around those skills.</p>
</div></div>
<section><div class="wrap brief">
<article class="article">
{STAMP}
<h2>What employers are mentioning</h2>
<p>In technology and finance, where vacancies fell and resident growth was slower, advertisements more often describe work you have already done on a named system or process. In care and essential services, they more often mention a registration, a language, or a shift pattern.</p>
<h2>SkillsFuture Credit</h2>
<p>Singapore citizens aged 25 and above have an opening SkillsFuture Credit of $500. You can use it on courses listed on MySkillsFuture, and it does not expire. Citizens aged 40 and above also have a mid-career credit of $4,000 for selected courses, which does not expire. From 1 December 2026, new runs of full Workforce Skills Qualifications and selected sector-agency courses join that mid-career list.</p>
<p>Your balance and which courses you can use it on are on MySkillsFuture, after a Singpass login. If someone offers to claim the credit for you and asks for your Singpass, a one-time password, or a fee up front, that is not how the official page works. You claim the credit yourself on the portal.</p>
<h2>Where the public lists are</h2>
<ul>
<li><a href="https://www.myskillsfuture.gov.sg/" rel="noopener">MySkillsFuture</a> for courses, credit, and subsidies.</li>
<li><a href="https://www.swda.gov.sg/" rel="noopener">Skills and Workforce Development Agency (SWDA)</a>, the statutory board formed from SkillsFuture Singapore and Workforce Singapore, in operation from 1 July 2026.</li>
<li>Connect by SWDA at the Lifelong Learning Institute, a public centre where you can talk about careers and skills.</li>
<li><a href="https://www.mycareersfuture.gov.sg/" rel="noopener">MyCareersFuture</a>, the government career portal, which also marks some roles tied to public career schemes.</li>
</ul>
<p>SkillsFuture Career Transition Programmes are train-and-place programmes aimed at sectors that are hiring. Places, sectors, and results change from one run to the next. The programme page explains what "place" means that time, including what happens if a match is not made. Finishing a programme and receiving an offer from an employer are two different things.</p>
<h2>What a course page usually tells you</h2>
<ul class="checks">
<li>Whether the same course, or a close one, is listed on MySkillsFuture.</li>
<li>The skill the course covers, and whether current advertisements in that sector mention it.</li>
<li>Who awards the certificate, and whether a regulator is involved.</li>
<li>Any request for Singpass, a one-time password, or a fee in order to unlock a government credit. The official route does not work that way.</li>
</ul>
<p class="src-note">The credit amounts and the 1 December 2026 mid-career course change come from SkillsFuture Credit guidance on MySkillsFuture. Your own balance is on that portal.</p>
</article>
<aside class="rail">
<h2>Alongside this</h2>
<ul>
<li><a href="industries.html">Industry guides</a></li>
<li><a href="applying.html">Applications</a></li>
<li><a href="career-path.html">Overview</a></li>
</ul>
</aside>
</div></section>
""",
)

PAGES["work-options.html"] = (
    "work",
    "Full-time, part-time, hybrid, online, contract and freelance work in Singapore | WorkNest SG",
    "A guide to full-time, part-time, hybrid, online, contract, project-based, and freelance work in Singapore's job market in late 2026.",
    f"""
<div class="page-head"><div class="wrap">
<p class="eyebrow">Work types · November 2026</p>
<h1><span>Full-time</span>, <span>part-time</span>, <span>hybrid</span>, <span>online</span>, <span>contract</span>, and <span>freelance</span> work.</h1>
<p class="lede">These are six arrangements people look for in Singapore, read against this quarter's labour figures. Full-time and part-time hiring is holding in care, transport, and public services. Hybrid, online, contract, project-based, and freelance work are easier to find in technology, finance, and professional services, where vacancies are thinner.</p>
</div></div>
<section><div class="wrap">
{STAMP}
<div class="tablewrap"><table>
<thead><tr><th>Work type</th><th>Where it shows up now</th><th>How it is usually set up</th></tr></thead>
<tbody>
<tr><td><a href="#full-time">Full-time work</a></td><td>Public services, care, and transport, where resident employment is still being supported.</td><td>A contract of service around a standard week, with leave, notice, and CPF.</td></tr>
<tr><td><a href="#part-time">Part-time work</a></td><td>Care, transport, essential services, and some roles beside a main job.</td><td>Under the Employment Act, fewer than 35 hours a week. The person remains an employee.</td></tr>
<tr><td><a href="#hybrid">Hybrid work</a></td><td>Technology and finance advertisements, even as vacancies in those sectors fell by June.</td><td>A mix of office and home days. The count of office days is part of the posting.</td></tr>
<tr><td><a href="#online">Online work</a></td><td>Technology, some professional services, and a share of freelance projects.</td><td>The work is done online. Many postings still name overlap hours or occasional office days.</td></tr>
<tr><td><a href="#contract">Contract and project-based work</a></td><td>Technology and professional services, in a quarter shaped by restructuring.</td><td>Employment or a project fee, often with an end date and a named employer.</td></tr>
<tr><td><a href="#freelance">Freelance work</a></td><td>Project work beside a main role, especially where firms are hiring more selectively.</td><td>Paid per project. CPF and tax follow the self-employed rules.</td></tr>
</tbody>
</table></div>
<div class="brief">
<article class="article">
<h2 id="full-time">Full-time work</h2>
<p>Full-time work is still the most common pattern in resident employment. In the third quarter of 2026, that resident growth was supported in public administration and education, transportation and storage, and health and social services. A full-time role is a contract of service, commonly around a standard week, with hours, overtime, leave, probation, and notice written into it.</p>
<p>In technology and finance, there were fewer vacancies by June. Financial services fell from 5,800 to 4,500, and information and communications from 5,300 to 4,400. Hiring there is selective. In care and public services it is steadier, and advertisements more often name shifts, registration, or a scheme window.</p>
<h2 id="part-time">Part-time work</h2>
<p>Under the Employment Act, part-time work is a contract for fewer than 35 hours a week. You are still an employee. Leave is pro-rated, and CPF for citizens and permanent residents applies once monthly wages are more than $50. The current CPF table is on the CPF Board site.</p>
<p>Part-time hours show up most clearly in care, transport, and essential services, the same sectors supporting resident employment this quarter. Some people also keep part-time work beside a full-time job, when the hours and the existing contract allow it. Pay depends on the hours that are actually rostered.</p>
<h2 id="hybrid">Hybrid work</h2>
<p>Hybrid work is a schedule: some days in an office, some days elsewhere. You will see it often in technology and finance advertisements. Those are also the sectors whose vacancies fell by June, and whose resident employment growth was slower in the third quarter. Even in a selective market, a hybrid posting usually says how many days are in the office.</p>
<p>Since 1 December 2024, someone already in a job can make a formal flexible-work request in writing. The employer has up to two months to reply. A reply is not the same as a yes. If you are applying for a new role, the arrangement on offer is the one written in the advertisement.</p>
<h2 id="online">Online work</h2>
<p>Online work means the tasks are done over the internet. You will see it in technology, in parts of professional services, and in freelance projects. MOM does not publish a separate count for online jobs, and many postings that say "online" still include overlap hours or a few days on site.</p>
<p>In information and communications, vacancies were 4,400 in June, down from 5,300 in March, and retrenchments in the second quarter rose from 530 to 720. Online arrangements are still being advertised inside that tighter market.</p>
<h2 id="contract">Contract and project-based work</h2>
<p>Contract and project-based work is either employment that ends on a date, or a fee for a defined piece of work. It is common in technology and professional services. Those sectors recorded resident gains in the second quarter and slower resident growth in the third. Business reorganisation was the main reason for retrenchments across the economy. A contract often names the employer, the end date, and whether it can end early. Those three lines are worth reading before you accept.</p>
<p>Project-based professional work — a memo, a model, a drawing set, a managed account — can mean you are employed by the firm, or employed by an agency and placed at the firm. Those are different CPF positions. Entry-level PMET vacancies, 31,700 in June, included professional services among the sectors in that group.</p>
<h2 id="freelance">Freelance work</h2>
<p>Freelance work is paid per project, and it is not employment. It shows up when a firm wants a defined piece of work without hiring another employee. That is easier to find this quarter in technology, finance, and professional services, where hiring is more selective. Some people also take freelance projects beside a full-time or part-time job.</p>
<p>CPF and tax on freelance income follow the self-employed rules published by CPF Board and IRAS. An advertisement that says "partner" can still be employment, or it can be freelance. CPF follows the type of contract, not the word in the headline. We do not estimate what freelance work pays. That depends on the project.</p>
<h2>CPF follows employment, including part-time</h2>
<p>If you are a Singapore citizen or permanent resident employed under a contract of service, and your total wages are more than $50 a month, your employer pays CPF. That includes part-time, temporary, and contract employees. Where monthly wages are above $50 and not more than $500, there is no employee share, and the employer still pays the employer share. Contributions are due by the 14th of the following month, or the next working day when the 14th falls on a weekend or public holiday. Rates change, including an increase for senior employees from 1 January 2027. The current table is on the CPF Board site.</p>
<p class="src-note">Sources: MOM Employment Act guidance on part-time employment; MOM Tripartite Guidelines on Flexible Work Arrangement Requests; CPF Board, saving as an employee; MOM labour market releases for the second and third quarters of 2026.</p>
</article>
<aside class="rail">
<h2>Alongside this</h2>
<ul>
<li><a href="industries.html">Industry guides</a></li>
<li><a href="applying.html">Applications</a></li>
<li><a href="market.html">National market</a></li>
</ul>
</aside>
</div>
</div></section>
""",
)

PAGES["applying.html"] = (
    "applying",
    "What job advertisements in Singapore usually contain | WorkNest SG",
    "What a Singapore job advertisement usually includes, where applications go, and which requests are worth treating with care.",
    f"""
<div class="page-head"><div class="wrap">
<p class="eyebrow">Applications</p>
<h1>What a job advertisement usually contains.</h1>
<p class="lede">A posting for full-time, part-time, hybrid, online, contract, or freelance work usually names an employer, the hours, the workplace, and how pay is calculated. You apply to that employer, or through a public portal such as MyCareersFuture. This site does not take CVs.</p>
</div></div>
<section><div class="wrap brief">
<article class="article">
{STAMP}
<h2>The market behind the advertisement</h2>
<p>The same CV can land differently depending on the sector. In technology and finance, the <a href="industries.html">industry guides</a> show fewer vacancies and more restructuring, so advertisements tend to be specific about systems and processes. In care and public services, resident employment is still being supported, and advertisements more often mention shifts, registration, or a scheme window.</p>
<p>Two advertisements with similar titles can still differ on hours and workplace. The duties inside them are often familiar tasks — scheduling, records, customer conversations, a named tool — even when your previous job title was different.</p>
<h2>What a first application usually includes</h2>
<p>A common application is about a page, unless the employer asks for more. It names the role, then a few tasks with some sense of scale: how often, for whom, and what changed. It often closes with the days and hours you can work, and when you could start. A photograph, NRIC number, passport details, bank details, and date of birth are rarely needed at this stage. If an employer wants a photograph, the advertisement says so.</p>
<h2>Where to send an application</h2>
<p>The employer's own careers page is the usual home of a role. MyCareersFuture, run by SWDA with GovTech, can be browsed without Singpass. Sending an application there uses Singpass and is for citizens and permanent residents. A repost on another board can point you toward a role. The copy on the employer's site, or on MyCareersFuture, is the one that matches the organisation. If a role appears in neither place, it is harder to check. A useful next step is the company's published address.</p>
<h2>Details that usually appear</h2>
<ul class="checks">
<li>The legal name of the employer, beyond a brand or a messaging-app room.</li>
<li>Employment or freelance, the hours, the workplace, and the pay basis: salary, hourly, or per project.</li>
<li>A closing date, where there is one, and the documents the posting asks for.</li>
<li>Cost. Ordinary employers do not charge a person to apply, to interview, or to release an offer.</li>
</ul>
<h2>Requests that are not part of ordinary hiring</h2>
<ul>
<li>A payment, a starter kit you have to buy, or a cheque you are asked to bank and partly return.</li>
<li>Your Singpass login, a one-time password, or a photo of your NRIC in the first conversation.</li>
<li>Bank details before a written offer from an employer you can identify.</li>
<li>An interview that exists only inside a personal messaging app, with no company email or published phone number.</li>
</ul>
<p>The ScamShield helpline is 1799. If money has already been lost, that report goes to the Police. ACRA's business-profile search shows whether a company name is on the register. A company can be registered and still not be offering a real job. If the name is not on the register at all, treat that as a warning sign.</p>
<h2>After you have applied</h2>
<p>It helps to keep a short record: the employer, the role, the date, the arrangement in the advertisement, and where you found it. Many applications do not lead to an interview. That is especially common in sectors MOM has described as selective. A later advertisement sometimes mentions a task the earlier application left out. Anyone who promises interviews in exchange for a fee is not using the public portals.</p>
<div class="callout"><p>Employment Act, CPF, and flexible-work details are published by MOM, CPF Board, and TAFEP. This page is the general pattern, not a substitute for those pages.</p></div>
</article>
<aside class="rail">
<h2>Alongside this</h2>
<ul>
<li><a href="work-options.html">Work arrangements</a></li>
<li><a href="skills.html">Skills and training</a></li>
<li><a href="updates.html">Update log</a></li>
</ul>
</aside>
</div></section>
""",
)

PAGES["updates.html"] = (
    "none",
    "Update log | WorkNest SG",
    "What changed in this Singapore job-market guide, and which official release the change follows.",
    """
<div class="page-head"><div class="wrap">
<p class="eyebrow">Update log</p>
<h1>What we revised, and why.</h1>
<p class="lede">Industry pages change when an official labour release changes the picture. Each page keeps the date of the release it follows.</p>
</div></div>
<section><div class="wrap article">
<ul class="log">
<li><time datetime="2026-11-19">19 November 2026</time>
<p>First set of market and industry guides. National employment, unemployment, retrenchment, and hiring intentions follow MOM's Labour Market Advance Release for the third quarter of 2026, released on 30 October 2026. Vacancy counts, the entry-level PMET definition, second-quarter retrenchment by sector, and the six-month re-entry rate follow the Labour Market Report for the second quarter of 2026, released on 21 September 2026.</p>
<p>SkillsFuture Credit amounts, the 1 December 2026 mid-career course change, SWDA's start on 1 July 2026, and the Tripartite flexible-work guidelines come from those agencies' public pages. They are rechecked when those pages change.</p>
<p>The Labour Market Report for the third quarter of 2026 is the next release MOM has pointed to, in mid-December 2026. It is expected to refresh sector splits, vacancies, turnover, and re-entry. Vacancy figures on this site remain labelled as June 2026 until then.</p>
</li>
</ul>
<p><a href="market.html">National market</a></p>
</div></section>
""",
)

PAGES["about.html"] = (
    "about",
    "About WorkNest SG",
    "WorkNest SG is an independent guide to Singapore's job market and how industries are hiring.",
    """
<div class="page-head"><div class="wrap">
<p class="eyebrow">About</p>
<h1>A guide to the market, updated when the figures move.</h1>
<p class="lede">WorkNest SG explains how full-time, part-time, hybrid, online, contract, project-based, and freelance work are showing up in Singapore, against the latest industry figures.</p>
</div></div>
<section><div class="wrap split">
<div>
<h2>What this is</h2>
<p>The guide covers the national labour figures, six industries, public training credits, work arrangements, and what an ordinary job advertisement contains. Each industry page follows an official release and shows the date of that release.</p>
<p>The site is independent of the Ministry of Manpower, the Skills and Workforce Development Agency, CPF Board, TAFEP, and employers. It does not list vacancies, and it does not recruit, screen, or place anyone.</p>
<h2>How a page changes</h2>
<p>We leave a figure in place until a newer official source replaces it. The review date is on the page. The <a href="updates.html">update log</a> names the release behind a change. If a later MOM report has replaced a number you still see here, you can tell us on the <a href="contact.html">contact</a> page.</p>
</div>
<div>
<h2>What this guide does not do</h2>
<ul>
<li>Promise a job, an interview, or a level of pay.</li>
<li>Present this site as a partner or representative of a government agency.</li>
<li>Take CVs, NRIC numbers, Singpass details, or money.</li>
<li>Estimate earnings.</li>
</ul>
<h2>Find us</h2>
<p>22 Orchard Road, #03-01, Singapore 238885<br>+65 8396 3756<br>support@worknestsg.com</p>
<p><a class="btn btn-primary" href="market.html">See the market</a></p>
</div>
</div></section>
""",
)

PAGES["contact.html"] = (
    "contact",
    "Contact WorkNest SG",
    "Write to us about a figure or a sector we have not covered. WorkNest SG does not take job applications.",
    """
<div class="page-head"><div class="wrap">
<p class="eyebrow">Contact</p>
<h1>Corrections and ideas for what to cover next.</h1>
<p class="lede">If a figure here has been overtaken, or a sector is missing, you can write to us. Job applications and CVs go to employers. This address does not pass them on.</p>
</div></div>
<section><div class="wrap split">
<div>
<p>Sending the form opens an email in your own mail app, addressed to support@worknestsg.com. We do not store the message on this website. You do not need to include an NRIC number, Singpass details, or bank information.</p>
<p>Phone: +65 8396 3756<br>22 Orchard Road, #03-01, Singapore 238885</p>
</div>
<div>
<form id="contact-form" class="form" novalidate>
<div class="field"><label for="name">Name</label><input id="name" name="name" autocomplete="name" required><div class="err" aria-live="polite"></div></div>
<div class="field"><label for="email">Email</label><input id="email" name="email" type="email" autocomplete="email" required><div class="err" aria-live="polite"></div></div>
<div class="field"><label for="topic">Topic</label><select id="topic" name="topic"><option>Correction to a figure</option><option>Industry to cover next</option><option>Question about the career path</option><option>Something else</option></select></div>
<div class="field"><label for="msg">Message</label><textarea id="msg" name="msg" required></textarea><div class="err" aria-live="polite"></div></div>
<button class="btn btn-primary" type="submit">Send message</button>
</form>
<div id="form-ok" class="ok" hidden tabindex="-1">
<h2>Your email app should be open.</h2>
<p>The message is addressed to support@worknestsg.com. If the app did not open, you can write to that address yourself.</p>
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
<p>This is general guidance, not personal advice. Current rules on the Employment Act, CPF, flexible work, and training credits are published by the Ministry of Manpower, CPF Board, IRAS, and the Skills and Workforce Development Agency.</p>
<h2>Sources and third parties</h2>
<p>We name the public source behind figures and link to official sites. We do not control those sites and we are not responsible for their content. We are not affiliated with them.</p>
<h2>Accuracy</h2>
<p>Each page is dated, and the <a href="updates.html">update log</a> records the release behind it. If a later official figure should replace one of ours, you can tell us on the <a href="contact.html">contact</a> page.</p>
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
<p>WorkNest SG is an independent information website. It publishes a job-market guide and industry guides. It is not an employment agency and it does not collect CVs for placement.</p>
<h2>2. Personal data we collect</h2>
<p>The contact form does not send data to our server. It opens an email in your own mail application. A message can include your name, your email address, and what you wanted to tell us. We do not ask for NRIC numbers, Singpass details, one-time passwords, bank details, or passwords.</p>
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
