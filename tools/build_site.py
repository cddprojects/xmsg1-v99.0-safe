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
<p>Notes on full-time, part-time, hybrid, online, contract, project-based, and freelance work in Singapore, set against the current job market.</p></div>
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
<p>WorkNest SG is an independent information site. It is not the Ministry of Manpower, the Skills and Workforce Development Agency, CPF Board, or an employment agency. It lists no vacancies and places no candidates. Figures describe the national market at the date shown. The notes are general information. ScamShield helpline: 1799.</p>
<p>&copy; 2026 WorkNest SG &middot; 22 Orchard Road, #03-01, Singapore 238885 &middot; +65 8396 3756 &middot; support@worknestsg.com</p>
</div>
</div></footer>
<script src="js/main.js"></script>
</body>
</html>
"""


def write(name: str, title: str, description: str, current: str, main: str) -> None:
    (ROOT / name).write_text(chrome(title, description, current, main), encoding="utf-8")


STAMP = """<p class="stamp"><strong>Updated 19 November 2026</strong><span>The next official sector and vacancy release is the MOM Labour Market Report for the third quarter of 2026, expected mid-December 2026.</span></p>"""

RAIL = """<aside class="rail">
<h2>About these figures</h2>
<ul>
<li>They describe the national quarter, and a single employer can look different.</li>
<li>Hours, workplace, and contract type sit in each advertisement.</li>
<li>A fee to be considered sits outside ordinary hiring.</li>
</ul>
<a class="back" href="market.html">National market note</a>
</aside>"""


PAGES = {}

PAGES["index.html"] = (
    "home",
    "Full-time, part-time, hybrid, online, contract and freelance work in Singapore | WorkNest SG",
    "Notes on full-time, part-time, hybrid, online, contract, project-based, and freelance work in Singapore, set against the latest job-market figures.",
    f"""
<section class="hero"><div class="wrap hero-grid">
<div>
<p class="eyebrow">Work types in Singapore · November 2026</p>
<h1>Full-time, part-time, hybrid, online, contract, and freelance work.</h1>
<p class="lede">These notes follow those six arrangements through the current market. Full-time and part-time hiring is still being supported in care, transport, and public services. Hybrid, online, contract, project-based, and freelance work show up more often in technology, finance, and professional services, where vacancies are thinner.</p>
<div class="btn-row"><a class="btn btn-primary" href="work-options.html">Work types</a><a class="btn btn-ghost" href="industries.html">By industry</a></div>
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
<div class="head"><p class="eyebrow">The six arrangements</p><h2>Where each kind of work sits this quarter.</h2>
<p class="lede">The labels follow the latest Ministry of Manpower picture. Pay and hours still depend on the role.</p></div>
<div class="cards">
<a class="card" href="work-options.html#full-time"><h3>Full-time work</h3><p>The main pattern in public services, care, and transport, where resident employment is still being supported.</p><span class="more">Current note</span></a>
<a class="card" href="work-options.html#part-time"><h3>Part-time work</h3><p>Under 35 hours a week. Common in care, transport, and essential services, and sometimes beside a full-time role.</p><span class="more">Current note</span></a>
<a class="card" href="work-options.html#hybrid"><h3>Hybrid work</h3><p>Still written into technology and finance advertisements, in a quarter when those vacancies fell.</p><span class="more">Current note</span></a>
<a class="card" href="work-options.html#online"><h3>Online work</h3><p>A place of work inside technology, professional services, and some freelance arrangements. Office days still appear in many postings.</p><span class="more">Current note</span></a>
<a class="card" href="work-options.html#contract"><h3>Contract and project-based work</h3><p>Common in technology and professional services, often with an end date, while those sectors restructure.</p><span class="more">Current note</span></a>
<a class="card" href="work-options.html#freelance"><h3>Freelance work</h3><p>Paid per project, outside employment. It shows up beside a main role, with self-employed CPF and tax rules.</p><span class="more">Current note</span></a>
</div>
</div></section>

<section><div class="wrap">
<div class="head"><p class="eyebrow">By industry</p><h2>The same arrangements, different sectors.</h2>
<p>A full-time care role and a hybrid technology role are meeting different markets this quarter.</p></div>
<div class="cards">
<a class="card" href="industry-care.html"><span class="pill steady">Steady</span><h3>Care and community</h3><p>Full-time and part-time shifts. Resident hiring in health and social services is still being supported.</p><span class="more">Current note</span></a>
<a class="card" href="industry-technology.html"><span class="pill cautious">Cautious</span><h3>Technology</h3><p>Hybrid, online, contract, and freelance work remain in advertisements. Vacancies fell, and resident hiring was subdued.</p><span class="more">Current note</span></a>
<a class="card" href="industry-finance.html"><span class="pill cautious">Cautious</span><h3>Finance</h3><p>Mostly full-time and hybrid. Vacancies fell from 5,800 to 4,500, and hiring is selective.</p><span class="more">Current note</span></a>
<a class="card" href="industry-professional.html"><span class="pill mixed">Mixed</span><h3>Professional services</h3><p>Project-based contracts, hybrid days, and some freelance work. Earlier resident gains cooled.</p><span class="more">Current note</span></a>
<a class="card" href="industry-logistics.html"><span class="pill mixed">Mixed</span><h3>Logistics and industry</h3><p>Full-time and part-time site work. Transport supported resident jobs. Online work is limited.</p><span class="more">Current note</span></a>
<a class="card" href="industry-public.html"><span class="pill steady">Steady</span><h3>Public and essential services</h3><p>Full-time schemes, with some part-time. This is where much of the resident employment growth sat.</p><span class="more">Current note</span></a>
</div>
</div></section>

<section class="alt"><div class="wrap split">
<div>
<p class="eyebrow">How the notes stay current</p>
<h2>Shared when the official figures move.</h2>
</div>
<div>
<p>Each industry page summarises the latest Ministry of Manpower release and names the source. A new labour market report updates the affected pages and the <a href="updates.html">update log</a> together.</p>
<p>Vacancy counts on this site remain the June 2026 figures until the third-quarter report arrives.</p>
<p><a href="about.html">About these notes</a></p>
</div>
</div></section>
""",
)

PAGES["career-path.html"] = (
    "path",
    "Notes on Singapore's job market | WorkNest SG",
    "Shared notes on Singapore's current job market, six industries, training credits, and how work arrangements are usually described.",
    f"""
<div class="page-head"><div class="wrap">
<p class="eyebrow">Overview</p>
<h1>Notes on a market that is moving in more than one direction.</h1>
<p class="lede">Full-time and part-time hiring is concentrated in essential and public services. Hybrid, online, contract, project-based, and freelance work are more visible in technology, finance, and professional services, where the quarter is quieter. The notes below stay with that split.</p>
</div></div>
<section><div class="wrap brief">
<article class="article">
{STAMP}
<h2>The national picture</h2>
<p>A rising employment total can be mostly work-permit hiring in construction and manufacturing, while resident hiring in technology or finance is quiet. The <a href="market.html">national note</a> keeps those two measures apart: total employment rose by 27,700 in the third quarter of 2026, and most of that increase was non-resident.</p>
<p>Sectors are also on different cycles. Care, transport and storage, and public services supported resident employment. Information and communications, financial services, and professional services had subdued resident growth in the same quarter.</p>
<h2>Industries</h2>
<p>The <a href="industries.html">industry notes</a> stay with one sector each. Scheduling, customer communication, records, and basic data work show up in more than one of them. The label on each note — steady, mixed, or cautious — follows the latest official release for that sector.</p>
<h2>Skills and training</h2>
<p>Advertisements and job titles describe overlapping tasks. A skill that shows up across several current advertisements is the sort of gap public catalogues are built around. A skill that shows up once is a narrower case. The <a href="skills.html">skills note</a> covers SkillsFuture Credit and the public course list, including the amounts and which courses they apply to.</p>
<h2>Work arrangements</h2>
<p>The word "flexible" in an advertisement can mean hybrid days, shift work, or freelance delivery. Those arrangements carry different CPF, leave, and tax patterns. The <a href="work-options.html">work arrangements</a> note sets out how part-time, contract, hybrid, and freelance work are usually defined in Singapore.</p>
<h2>Applications</h2>
<p>Advertisements usually name an employer, hours, a workplace, and a pay basis. Some messages also ask for a fee, a Singpass login, a one-time password, or a conversation that exists only in a messaging app. The <a href="applying.html">applications</a> note describes both the ordinary contents and those other requests.</p>
<h2>Dates on the notes</h2>
<p>Each industry page carries the date it was last aligned to an official release. The <a href="updates.html">update log</a> records which release that was. The next fuller sector report is expected in mid-December 2026.</p>
<div class="callout"><p>Connect by SWDA, at the Lifelong Learning Institute, is a public centre for career and skills conversations. These notes are independent of that service.</p></div>
</article>
<aside class="rail">
<h2>In the notes</h2>
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
<li>Technology, finance, and professional services had subdued resident growth.</li>
<li>Vacancy counts below are the June 2026 figures. The newer vacancy release is still ahead.</li>
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
<p>Among residents retrenched in the second quarter, 54.9% were back in employment within six months, down from 60.7% in the first quarter. The twelve-month re-entry rate was 69.8%. The six-month rate can be lower even while the unemployment rate stays low. Both figures describe groups, and a single search can sit anywhere inside them.</p>
<h2>Vacancies, as of June</h2>
<p>Job vacancies fell from 73,300 in March 2026 to 68,600 in June, and from 76,200 in June 2025. The vacancy rate was 2.8%. The largest declines were in financial services (5,800 to 4,500) and information and communications (5,300 to 4,400).</p>
<p>Entry-level PMET vacancies were 31,700 in June, 45.3% of all vacancies. MOM describes these as professional, manager, executive, and technician vacancies advertised with a minimum salary between $2,300 and $5,000, spanning sectors such as health and social services and professional services. The range is the survey's definition of that group.</p>
<h2>What employers said they might do next</h2>
<p>In September 2026, 42.3% of firms expected to hire in the next three months, up from 30.5% in August. The share expecting to raise wages rose from 16.9% to 19.9%. The share expecting to retrench rose from 2.8% to 3.1%. MOM said hiring and wage expectations improved in September but stayed below July's levels, and that firms remained selective.</p>
<div class="callout"><p>The third-quarter Labour Market Report, expected in mid-December 2026, will add sector employment splits, vacancy counts, turnover, and re-entry rates. Vacancy numbers on this site remain the June figures until that report.</p></div>
<h2>Sources</h2>
<ul class="sources">
<li><a href="https://www.mom.gov.sg/newsroom/press-releases/2026/1030-labour-market-advance-release-3q-2026" rel="noopener">MOM: Labour Market Advance Release, third quarter 2026 (30 October 2026)</a></li>
<li><a href="https://www.mom.gov.sg/newsroom/press-releases/2026/0921-labour-market-report---second-quarter-2026" rel="noopener">MOM: Labour Market Report, second quarter 2026 (21 September 2026)</a></li>
<li><a href="https://stats.mom.gov.sg/iMAS_PdfLibrary/mrsd-Labour-Market-Report-2Q-2026.pdf" rel="noopener">MOM Manpower Research and Statistics Department, Labour Market Report 2Q 2026 (PDF)</a></li>
</ul>
<p><a href="industries.html">Industry notes</a></p>
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
<p>Advertisements in this sector usually state the workplace, the shift pattern, and whether the role is employment or a contract for service. Part-time care work under a contract of service remains employment. CPF for Singapore citizens and permanent residents in that kind of employment applies when monthly wages are more than $50. The current table is published by CPF Board.</p>
<p>Where a role is regulated, the meaning of "registered" or "enrolled" is set out on the regulator's own site. Descriptions of care roles commonly mention shift attendance, records, and work with families.</p>
""",
        ["Registration or enrolment, where the role is regulated.", "Shift pattern, including nights, weekends, and how far ahead the roster is published.", "Employment or freelance, and which party pays CPF.", "Site location. Community roles are often spread across several centres."],
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
<p>Advertisements still mention data, cloud, cyber, and applied AI work. In a quarter shaped by restructuring, those advertisements more often describe a tool inside a real workflow than a list of product names.</p>
""",
        """
<p>Openings are fewer than a year earlier. The advertisements that remain tend to name a system, the size of the workload, and what changed. Remote days and contract terms appear in individual advertisements. They are a feature of that advertisement, and the sector as a whole still includes office-based employment.</p>
<p>On 16 September 2026, SWDA published a public catalogue of more than 200 AI-related courses, with a time-limited tool subscription for eligible citizens who enrol and attend. Eligibility is described on SWDA's own pages. The catalogue is a training list.</p>
""",
        ["The product or system, and the part of the work attached to it.", "Permanent employment, a contract, or a vendor placement, and the employer of record.", "Office days, time-zone overlap, and on-call hours.", "Any fee for equipment, a starter kit, or a training seat in order to be considered."],
    ),
    (
        "industry-finance.html",
        "Finance jobs in Singapore: late 2026 market | WorkNest SG",
        "Financial services in late 2026: fewer vacancies, more restructuring, and subdued resident employment growth.",
        "cautious",
        "Fewer vacancies, more restructuring",
        "Finance",
        "Financial services is hiring selectively, not broadly.",
        """
<p>Financial services vacancies fell from 5,800 in March 2026 to 4,500 in June, one of the two largest sector declines in that quarter. Retrenchments in the sector rose from 560 in the first quarter to 710 in the second. Business reorganisation was the main reason for retrenchments across the economy.</p>
<p>In the third quarter, resident employment growth in financial services was subdued. The second quarter had still shown resident gains. Against a 2025 picture of the sector, the later figures show fewer vacancies and smaller teams in some areas, with the remaining advertisements filled more selectively.</p>
<p>Public descriptions of the sector still include operations, compliance, risk, finance change, and client servicing. Those are the kinds of work the sector talks about. The vacancy count says how many seats were open in June.</p>
""",
        """
<p>Advertisements that are still open often name a regulation, a product, or a process, such as reconciliations, case handling, vendor checks, or management information. Hybrid wording is common, and the number of office days is usually in the same advertisement. A role described as flexible can still require every day in the office. That schedule is part of the role.</p>
<p>Some client-facing and representative roles refer to a licence. The Monetary Authority of Singapore keeps public registers for those roles, and advertisements sometimes say whether a licence is required or sponsored.</p>
""",
        ["The employer of record, including where a posting comes through an agency.", "Any licence or certification, and which party pays for it.", "Office days and the hours someone is expected to be reachable.", "Pay as base salary, allowance, or commission, and what the commission depends on."],
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
<p>Professional services recorded resident employment gains in the second quarter of 2026, along with other outward-oriented sectors. In the third quarter, resident growth in the sector was subdued. The two quarters together show a cooler market than the second quarter on its own.</p>
<p>In June, entry-level PMET vacancies spanned sectors including professional services and health and social services. Those 31,700 vacancies were roles advertised with a minimum salary between $2,300 and $5,000. The pool is a statistical group. It describes advertised minimums, and firms differ inside it.</p>
<p>The sector covers legal, accounting, management consulting, architecture, and engineering. A slow quarter in one practice can sit next to a steadier one. Advertisements in the specific practice carry more detail than the sector label.</p>
""",
        """
<p>Advertisements in this sector often refer to a piece of client work: a memo, a model, a drawing set, a managed account. Titles such as "associate" mean different things from one firm to another. Project-based contracts are common, and the length, early-end terms, and the employer — the firm itself, or a staffing company — change the pay and CPF position.</p>
<p>The <a href="skills.html">skills note</a> sets out SkillsFuture Credit and the public course list that sit beside these advertisements.</p>
""",
        ["Employment by the firm, or employment by an agency with deployment to the firm.", "Utilisation or billing expectations, where the advertisement mentions them.", "The qualification route for regulated work such as accounting or engineering, as published by the professional body.", "Whether a project end date is also the employment end date."],
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
<p>June vacancy figures for these sectors are due for a refresh in the mid-December report. Until then, the employment and retrenchment split above is the later evidence.</p>
""",
        """
<p>Advertisements in transport and warehousing often turn on licence class, shift, and site. In manufacturing, production-operator roles and technician or engineer roles are different advertisements. Retrenchment has been higher here than in care or public services, and contract length is often part of the same posting.</p>
<p>Safety orientation and site access sit inside the job. A request for payment for a "site pass" before a named employer has confirmed the role in writing is outside that ordinary pattern. The employer's own channel is where the role, if it is real, also appears.</p>
""",
        ["The licence or certificate named in the advertisement.", "Shift hours, overtime practice, and the work site.", "Employment, daily-rated work, or a freelance arrangement.", "Which party issues any pass or permit, and whether a fee is attached."],
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
<p>MOM's third-quarter advance release said resident employment growth continued to be supported mainly by essential and public services, naming public administration and education, transportation and storage, and health and social services. This note covers the public-administration and education part. Care and transport have their own pages because the day-to-day work is different.</p>
<p>Hiring here often follows budget cycles, schemes, and fixed windows, rather than a rolling private-sector advertisement. A quiet week on a job portal can simply be the gap between windows.</p>
<p>Second-quarter retrenchment increases were concentrated elsewhere. The published figures for public administration and education were quiet on that measure. A single agency can still differ from the sector total.</p>
""",
        """
<p>Scheme details usually live on the agency's own site or on Careers@Gov, as well as on any repost. Citizenship conditions, medical or security checks, and closing dates are commonly part of those pages.</p>
<p>Education roles can involve a qualification, a registration, or both. Early-childhood and school roles are different schemes. Eligibility pages on the relevant agency describe what a certificate is for. Mid-career schemes sometimes recognise occupational experience and sometimes use a trainee pay point. The advertisement is where that distinction is written.</p>
""",
        ["The closing date, and whether late applications are accepted.", "Citizenship or residency conditions.", "Registration, medical, or security clearance, where the scheme includes them.", "The pay point for mid-career entrants, where the scheme publishes one."],
    ),
]


def industry_page(slug, title, description, pill, pill_label, h_label, lede, situation, applying, checks):
    items = "".join(f"<li>{c}</li>" for c in checks)
    return f"""
<div class="page-head"><div class="wrap">
<p class="eyebrow">Industry note · {h_label}</p>
<h1>{lede}</h1>
<p class="lede"><span class="pill {pill}">{pill_label}</span></p>
</div></div>
<section><div class="wrap brief">
<article class="article">
{STAMP}
<h2>The situation</h2>
{situation}
<h2>How the work is usually described</h2>
{applying}
<h2>Details that often appear in advertisements</h2>
<ul class="checks">{items}</ul>
<p class="src-note">National figures: MOM Labour Market Advance Release, third quarter 2026, and Labour Market Report, second quarter 2026. This note shares that public picture.</p>
<p><a href="industries.html">All industries</a> · <a href="applying.html">Applications</a></p>
</article>
{RAIL}
</div></section>
"""


PAGES["industries.html"] = (
    "industries",
    "Industry notes on Singapore's job market | WorkNest SG",
    "How full-time, part-time, hybrid, online, contract, and freelance work show up in care, technology, finance, and other Singapore sectors.",
    """
<div class="page-head"><div class="wrap">
<p class="eyebrow">Industries</p>
<h1>Where full-time, hybrid, online, and freelance work are showing up.</h1>
<p class="lede">Each note stays with one sector and the arrangements advertisements there usually name: full-time, part-time, hybrid, online, contract or project-based, and freelance.</p>
</div></div>
<section><div class="wrap">
<p class="stamp"><strong>Updated 19 November 2026</strong><span>Vacancy counts are from June 2026 until the third-quarter report is published.</span></p>
<div class="cards">
<a class="card" href="industry-care.html"><span class="pill steady">Steady</span><h3>Care and community</h3><p>Full-time and part-time shifts. Resident employment in health and social services is still being supported.</p><span class="more">Current note</span></a>
<a class="card" href="industry-technology.html"><span class="pill cautious">Cautious</span><h3>Technology</h3><p>Hybrid, online, contract, and freelance advertisements, with fewer vacancies and subdued resident growth.</p><span class="more">Current note</span></a>
<a class="card" href="industry-finance.html"><span class="pill cautious">Cautious</span><h3>Finance</h3><p>Full-time and hybrid work. Vacancies fell from 5,800 to 4,500, and hiring is selective.</p><span class="more">Current note</span></a>
<a class="card" href="industry-professional.html"><span class="pill mixed">Mixed</span><h3>Professional services</h3><p>Project-based contracts, hybrid days, and some freelance work. Earlier resident gains cooled.</p><span class="more">Current note</span></a>
<a class="card" href="industry-logistics.html"><span class="pill mixed">Mixed</span><h3>Logistics and industry</h3><p>Full-time and part-time site work. Transport supported resident jobs. Online work is limited.</p><span class="more">Current note</span></a>
<a class="card" href="industry-public.html"><span class="pill steady">Steady</span><h3>Public and essential services</h3><p>Full-time schemes, with some part-time hours. Resident employment growth was supported here.</p><span class="more">Current note</span></a>
</div>
<p style="margin-top:1.4rem"><a href="market.html">National market note behind these labels</a></p>
</div></section>
""",
)

PAGES["skills.html"] = (
    "none",
    "Skills and training for job applications in Singapore | WorkNest SG",
    "SkillsFuture Credit, public courses, and how training sits beside Singapore's current job market.",
    f"""
<div class="page-head"><div class="wrap">
<p class="eyebrow">Skills and training</p>
<h1>Training sits beside the market, in public catalogues.</h1>
<p class="lede">In a quarter when some sectors are hiring more carefully, advertisements tend to name a specific skill, a registration, or a shift pattern. Public credits and course lists describe what is available around those skills.</p>
</div></div>
<section><div class="wrap brief">
<article class="article">
{STAMP}
<h2>What the market is asking for</h2>
<p>In technology and finance, where vacancies fell and resident growth was subdued, advertisements more often describe work already done on a named system or process. In care and essential services, advertisements more often mention a registration, a language, or a shift pattern.</p>
<h2>SkillsFuture Credit</h2>
<p>Singapore citizens aged 25 and above have an opening SkillsFuture Credit of $500. It can be used on courses listed on the MySkillsFuture portal, and it does not expire. Citizens aged 40 and above also have a mid-career credit of $4,000 for selected courses, which does not expire. From 1 December 2026, new course runs of full Workforce Skills Qualifications and selected sector-agency courses join the mid-career list.</p>
<p>Balances and course eligibility appear on MySkillsFuture with a Singpass login. A message that offers to "claim the credit" in exchange for a Singpass login, a one-time password, or an upfront fee sits outside that official page. Claims go through the portal itself.</p>
<h2>Public places the lists live</h2>
<ul>
<li><a href="https://www.myskillsfuture.gov.sg/" rel="noopener">MySkillsFuture</a> for courses, credit, and subsidies.</li>
<li><a href="https://www.swda.gov.sg/" rel="noopener">Skills and Workforce Development Agency (SWDA)</a>, the statutory board formed from SkillsFuture Singapore and Workforce Singapore, in operation from 1 July 2026.</li>
<li>Connect by SWDA at the Lifelong Learning Institute, a public centre for career and skills conversations.</li>
<li><a href="https://www.mycareersfuture.gov.sg/" rel="noopener">MyCareersFuture</a>, the government career portal, which also marks some roles tied to public career schemes.</li>
</ul>
<p>SkillsFuture Career Transition Programmes are train-and-place programmes aimed at sectors with hiring opportunities. Places, sectors, and outcomes change. The current programme page describes what "place" means in that run, including the position when a match is not made. Completion of a programme and an employer's offer are separate events.</p>
<h2>What usually sits on a course page</h2>
<ul class="checks">
<li>Whether the same course, or a close one, is listed on MySkillsFuture.</li>
<li>The skill the course covers, and whether current advertisements in that sector mention it.</li>
<li>The body that awards the certificate, and whether a regulator is involved.</li>
<li>Any request for Singpass, a one-time password, or a fee in order to unlock a government credit.</li>
</ul>
<p class="src-note">Credit amounts and the 1 December 2026 mid-career course change come from SkillsFuture Credit guidance on MySkillsFuture. A personal balance is on that portal.</p>
</article>
<aside class="rail">
<h2>Alongside this</h2>
<ul>
<li><a href="industries.html">Industry notes</a></li>
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
    "How full-time, part-time, hybrid, online, contract, project-based, and freelance work are showing up in Singapore's job market in late 2026.",
    f"""
<div class="page-head"><div class="wrap">
<p class="eyebrow">Work types · November 2026</p>
<h1>Full-time, part-time, hybrid, online, contract, and freelance work.</h1>
<p class="lede">Six arrangements people look for in Singapore, set against this quarter's labour figures. Full-time and part-time hiring is holding in care, transport, and public services. Hybrid, online, contract, project-based, and freelance work are more visible in technology, finance, and professional services, where vacancies are thinner.</p>
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
<p>Full-time work is still the largest pattern in resident employment. In the third quarter of 2026, that resident growth was supported in public administration and education, transportation and storage, and health and social services. A full-time role is a contract of service, commonly around a standard week, with hours, overtime, leave, probation, and notice written into it.</p>
<p>In technology and finance, vacancies were fewer by June. Financial services fell from 5,800 to 4,500, and information and communications from 5,300 to 4,400. Hiring there is selective. In care and public services it is steadier, and advertisements more often name shifts, registration, or a scheme window.</p>
<h2 id="part-time">Part-time work</h2>
<p>Part-time work, under the Employment Act, is a contract for fewer than 35 hours a week. It is still employment. Pro-rated leave and CPF for citizens and permanent residents follow from that, once monthly wages are more than $50. The current CPF table is on the CPF Board site.</p>
<p>Part-time hours show up most clearly in care, transport, and essential services, the same sectors supporting resident employment this quarter. Some people also keep part-time work beside a full-time role when the hours and the existing contract allow it. Pay depends on the hours that are actually rostered.</p>
<h2 id="hybrid">Hybrid work</h2>
<p>Hybrid work is a schedule: some days in an office, some days elsewhere. It is common language in technology and finance advertisements. Those are also the sectors whose vacancies fell by June, and whose resident employment growth was subdued in the third quarter. A hybrid posting in a selective market still names the office days.</p>
<p>Formal flexible-work requests have had a written process since 1 December 2024. The employer has up to two months to respond. The guidelines describe the process. Agreement is a separate decision, and the pattern in a job advertisement is the one on offer for a new role.</p>
<h2 id="online">Online work</h2>
<p>Online work means the tasks are done over the internet. It appears in technology, in parts of professional services, and in freelance projects. It is a feature of those advertisements. The national figures do not publish a separate count for online jobs, and many postings that say online still include overlap hours or a few days on site.</p>
<p>In information and communications, vacancies were 4,400 in June, down from 5,300 in March, and retrenchments in the second quarter rose from 530 to 720. Online arrangements are still being advertised inside that tighter market.</p>
<h2 id="contract">Contract and project-based work</h2>
<p>Contract and project-based work is employment that ends on a date, or a fee for a defined piece of work. It is common in technology and professional services. Those sectors recorded resident gains in the second quarter and subdued resident growth in the third, and business reorganisation was the main reason for retrenchments across the economy. A contract often names the employer, the end date, and whether it can end early.</p>
<p>Project-based professional work — a memo, a model, a drawing set, a managed account — can be employment by the firm or employment by an agency deployed to the firm. Those are different CPF positions. Entry-level PMET vacancies, 31,700 in June, included professional services among the sectors in that pool.</p>
<h2 id="freelance">Freelance work</h2>
<p>Freelance work is paid per project and sits outside employment. It shows up where firms want a defined deliverable without adding a headcount, which fits a quarter of selective hiring in technology, finance, and professional services. It also shows up beside a full-time or part-time role.</p>
<p>CPF and tax for freelance income follow the self-employed rules published by CPF Board and IRAS. An advertisement that says "partner" can still be employment, or it can be freelance. The contract type is what the CPF position follows. These notes do not estimate freelance earnings.</p>
<h2>CPF follows employment, including part-time</h2>
<p>A Singapore citizen or permanent resident employed under a contract of service, with total wages of more than $50 a month, is in the group whose employer pays CPF. That includes part-time, temporary, and contract employees. Where monthly wages are above $50 and not more than $500, there is no employee share, and the employer still pays the employer share. Contributions are due by the 14th of the following month, or the next working day when the 14th falls on a weekend or public holiday. Rates change, including an increase for senior employees from 1 January 2027. The current table is on the CPF Board site.</p>
<p class="src-note">Sources: MOM Employment Act guidance on part-time employment; MOM Tripartite Guidelines on Flexible Work Arrangement Requests; CPF Board, saving as an employee; MOM labour market releases for the second and third quarters of 2026.</p>
</article>
<aside class="rail">
<h2>Alongside this</h2>
<ul>
<li><a href="industries.html">Industry notes</a></li>
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
    "A shared note on what Singapore job advertisements usually include, where applications go, and which requests sit outside ordinary hiring.",
    f"""
<div class="page-head"><div class="wrap">
<p class="eyebrow">Applications</p>
<h1>What a job advertisement usually contains.</h1>
<p class="lede">A posting for full-time, part-time, hybrid, online, contract, or freelance work usually names an employer, the hours, the workplace, and how pay is calculated. Applications go to that employer, or through a public portal such as MyCareersFuture. This site does not receive CVs.</p>
</div></div>
<section><div class="wrap brief">
<article class="article">
{STAMP}
<h2>The market behind the advertisement</h2>
<p>The same CV meets a different market depending on the sector. In technology and finance, the <a href="industries.html">industry notes</a> show fewer vacancies and more restructuring, so advertisements tend to be specific about systems and processes. In care and public services, resident employment is still being supported, and advertisements more often mention shifts, registration, or a scheme window.</p>
<p>Two advertisements for similar titles can still differ on hours and workplace. The duties inside them are often shared tasks — scheduling, records, customer conversations, a named tool — even when the old job title was different.</p>
<h2>What applications commonly include</h2>
<p>A common application is about a page, unless the employer asks for more. It names the role, then a few tasks with some scale: how often, for whom, and what changed. It often closes with the days, hours, and start date the person can work. Photographs, NRIC numbers, passport details, bank details, and dates of birth are rarely part of that first note. Employers that want a photograph say so.</p>
<h2>Where applications go</h2>
<p>The employer's own careers page is the usual home of a role. MyCareersFuture, run by SWDA with GovTech, can be browsed without Singpass. Sending an application there uses Singpass and is for citizens and permanent residents. A repost on another board can point toward a role. The posting on the employer's site, or on MyCareersFuture, is the copy that matches the organisation. A role that appears in neither place is harder to trace, and the company's published address is where that trace usually starts.</p>
<h2>Details that usually appear</h2>
<ul class="checks">
<li>The legal name of the employer, beyond a brand or a messaging-app room.</li>
<li>Employment or freelance, the hours, the workplace, and the pay basis: salary, hourly, or per project.</li>
<li>A closing date, where there is one, and the documents the posting asks for.</li>
<li>Cost. Ordinary employers do not charge a person to apply, to interview, or to release an offer.</li>
</ul>
<h2>Requests that sit outside ordinary hiring</h2>
<ul>
<li>Payment, a starter kit that has to be bought, or a cheque to bank and partly return.</li>
<li>A Singpass login, a one-time password, or an NRIC photo in the first conversation.</li>
<li>Bank details before a written offer from an employer whose name can be traced.</li>
<li>An interview that exists only inside a personal messaging app, with no company email or published phone number.</li>
</ul>
<p>The ScamShield helpline is 1799. Reports of lost money go to the Police. ACRA's business-profile search shows whether a company name is on the register. A registration and a genuine offer are separate facts. A name that is missing from the register is a gap in that trace.</p>
<h2>After an application goes out</h2>
<p>People often keep a short record: employer, role, date, the arrangement in the advertisement, and where it was found. Many applications draw no interview. That pattern is especially visible in sectors MOM has described as selective. Later advertisements sometimes mention a task the earlier application left out. A third party that promises interviews in exchange for a fee sits outside the public portals.</p>
<div class="callout"><p>Employment Act, CPF, and flexible-work details are published by MOM, CPF Board, and TAFEP. This note shares the general pattern.</p></div>
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
    "What changed in WorkNest SG's Singapore job-market notes, and which official release the change follows.",
    """
<div class="page-head"><div class="wrap">
<p class="eyebrow">Update log</p>
<h1>What we revised, and why.</h1>
<p class="lede">Industry pages move when an official labour release changes the picture. Each note keeps the date of the release it follows.</p>
</div></div>
<section><div class="wrap article">
<ul class="log">
<li><time datetime="2026-11-19">19 November 2026</time>
<p>First set of market and industry notes. National employment, unemployment, retrenchment, and hiring intentions follow MOM's Labour Market Advance Release for the third quarter of 2026, released on 30 October 2026. Vacancy counts, the entry-level PMET definition, second-quarter retrenchment by sector, and the six-month re-entry rate follow the Labour Market Report for the second quarter of 2026, released on 21 September 2026.</p>
<p>SkillsFuture Credit amounts, the 1 December 2026 mid-career course change, SWDA's start on 1 July 2026, and the Tripartite flexible-work guidelines come from those agencies' public pages. They are rechecked when those pages change.</p>
<p>The Labour Market Report for the third quarter of 2026 is the next release MOM has pointed to, in mid-December 2026. It is expected to refresh sector splits, vacancies, turnover, and re-entry. Vacancy figures on this site remain labelled as June 2026 until then.</p>
</li>
</ul>
<p><a href="market.html">National market note</a></p>
</div></section>
""",
)

PAGES["about.html"] = (
    "about",
    "About WorkNest SG",
    "WorkNest SG shares dated notes on Singapore's job market and how industries are hiring.",
    """
<div class="page-head"><div class="wrap">
<p class="eyebrow">About</p>
<h1>Notes on the market, updated when the figures move.</h1>
<p class="lede">WorkNest SG shares how full-time, part-time, hybrid, online, contract, project-based, and freelance work are showing up in Singapore, against the latest industry figures.</p>
</div></div>
<section><div class="wrap split">
<div>
<h2>What this is</h2>
<p>The notes cover the national labour figures, six industries, public training credits, work arrangements, and the contents of ordinary job advertisements. Each industry page follows an official release and carries the date of that release.</p>
<p>The site is independent of the Ministry of Manpower, the Skills and Workforce Development Agency, CPF Board, TAFEP, and employers. It lists no vacancies and handles no recruitment, screening, or placement.</p>
<h2>How a page changes</h2>
<p>A figure stays while its source is the latest one checked. The review date is on the page. The <a href="updates.html">update log</a> names the release behind the change. A number that a later MOM report has replaced can be flagged through the <a href="contact.html">contact</a> page.</p>
</div>
<div>
<h2>Outside the scope of these notes</h2>
<ul>
<li>A promise of a job, an interview, or a level of pay.</li>
<li>Any description of this site as a partner or representative of a government agency.</li>
<li>CVs, NRIC numbers, Singpass details, or money.</li>
<li>An estimate of earnings.</li>
</ul>
<h2>Find us</h2>
<p>22 Orchard Road, #03-01, Singapore 238885<br>+65 8396 3756<br>support@worknestsg.com</p>
<p><a class="btn btn-primary" href="market.html">Market note</a></p>
</div>
</div></section>
""",
)

PAGES["contact.html"] = (
    "contact",
    "Contact WorkNest SG",
    "Notes about a figure or a missing sector. WorkNest SG does not take job applications.",
    """
<div class="page-head"><div class="wrap">
<p class="eyebrow">Contact</p>
<h1>Corrections and topic ideas.</h1>
<p class="lede">A superseded figure or a missing sector can be sent here. Job applications and CVs go to employers, and this address does not forward them.</p>
</div></div>
<section><div class="wrap split">
<div>
<p>The form opens an email in the visitor's own mail app, addressed to support@worknestsg.com. Nothing is stored on this website. NRIC numbers, Singpass details, and bank information are not needed for a note about the site.</p>
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
<h2>The message is in the email app.</h2>
<p>It is addressed to support@worknestsg.com. The same address works if the app did not open.</p>
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
<p>The notes are general information. Current rules on the Employment Act, CPF, flexible work, and training credits are published by the Ministry of Manpower, CPF Board, IRAS, and the Skills and Workforce Development Agency.</p>
<h2>Sources and third parties</h2>
<p>We name the public source behind figures and link to official sites. We do not control those sites and we are not responsible for their content. We are not affiliated with them.</p>
<h2>Accuracy</h2>
<p>Each note is dated, and the <a href="updates.html">update log</a> records the release behind it. A later official figure can be flagged on the <a href="contact.html">contact</a> page.</p>
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
<p>WorkNest SG is an independent information website. It publishes market notes and industry notes. It is not an employment agency and it does not collect CVs for placement.</p>
<h2>2. Personal data we collect</h2>
<p>The contact form does not send data to our server. It opens an email in the visitor's own mail application. A message can include a name, an email address, and the note itself. NRIC numbers, Singpass details, one-time passwords, bank details, and passwords are not part of that note, and this site does not ask for them.</p>
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
