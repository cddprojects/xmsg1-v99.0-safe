#!/usr/bin/env python3
"""Build the WorkNest SG blog as static HTML."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "site"

PUBLISHED = "19 November 2026"
PUBLISHED_ISO = "2026-11-19"
BYLINE = "WorkNest SG Editorial"

BRAND = """<svg viewBox="0 0 32 32" aria-hidden="true"><rect width="32" height="32" rx="9" fill="#1f5a4f"/><path d="M6 16.5 16 7l10 9.5" stroke="#f6f3ec" stroke-width="2.4" fill="none" stroke-linecap="round" stroke-linejoin="round"/><path d="M9.5 15v9h13v-9" fill="#f6f3ec"/><circle cx="16" cy="19.5" r="2.4" fill="#c4553a"/></svg>Work<em>Nest</em> SG"""

NAV = [
    ("index.html", "Home", "home"),
    ("work-options.html", "Work types", "work"),
    ("industries.html", "Industries", "industries"),
    ("market.html", "Market", "market"),
    ("articles.html", "All articles", "articles"),
    ("about.html", "About", "about"),
    ("contact.html", "Contact", "contact"),
]

CATEGORY_HUB = {
    "Work types": ("work-options.html", "work"),
    "Industry report": ("industries.html", "industries"),
    "Market review": ("market.html", "market"),
    "Practical guide": ("articles.html", "articles"),
}


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
<p>An independent Singapore blog on full-time, part-time, hybrid, online, contract, project-based, and freelance work, written from the latest official labour figures.</p></div>
<div><h2>Work types series</h2><ul>
<li><a href="full-time-work.html">Full-time work</a></li>
<li><a href="part-time-work.html">Part-time work</a></li>
<li><a href="hybrid-work.html">Hybrid work</a></li>
<li><a href="online-work.html">Online work</a></li>
<li><a href="contract-work.html">Contract and project work</a></li>
<li><a href="freelance-work.html">Freelance work</a></li>
</ul></div>
<div><h2>Reporting</h2><ul>
<li><a href="market.html">Quarterly market review</a></li>
<li><a href="industries.html">Industry reports</a></li>
<li><a href="applying.html">Reading a job advertisement</a></li>
<li><a href="skills.html">SkillsFuture Credit in 2026</a></li>
<li><a href="articles.html">All articles</a></li>
</ul></div>
<div><h2>WorkNest SG</h2><ul>
<li><a href="about.html">About the blog</a></li>
<li><a href="updates.html">Editor's log</a></li>
<li><a href="contact.html">Contact</a></li>
<li><a href="privacy.html">Privacy</a></li>
<li><a href="disclaimer.html">Disclaimer</a></li>
</ul></div>
</div>
<div class="legal">
<p>WorkNest SG is an independent publication. It is not the Ministry of Manpower, the Skills and Workforce Development Agency, CPF Board, or an employment agency. It does not list vacancies or place candidates. Figures describe the national market on the date stated, and articles are general information rather than personal advice. ScamShield helpline: 1799.</p>
<p>&copy; 2026 WorkNest SG &middot; 22 Orchard Road, #03-01, Singapore 238885 &middot; +65 8396 3756 &middot; support@worknestsg.com</p>
</div>
</div></footer>
<script src="js/main.js"></script>
</body>
</html>
"""


def write(name: str, title: str, description: str, current: str, main: str) -> None:
    (ROOT / name).write_text(chrome(title, description, current, main), encoding="utf-8")


def reading_minutes(html: str) -> int:
    words = len(re.sub(r"<[^>]+>", " ", html).split())
    return max(2, round(words / 220))


def figbox(rows) -> str:
    items = "".join(f"<li><b>{n}</b><span>{t}</span></li>" for n, t in rows)
    return f'<div class="figbox"><h2>Key figures</h2><ul>{items}</ul><p>Ministry of Manpower releases for the second and third quarters of 2026.</p></div>'


SOURCES_MOM = [
    ("https://www.mom.gov.sg/newsroom/press-releases/2026/1030-labour-market-advance-release-3q-2026", "Ministry of Manpower, Labour Market Advance Release, third quarter 2026 (30 October 2026)"),
    ("https://www.mom.gov.sg/newsroom/press-releases/2026/0921-labour-market-report---second-quarter-2026", "Ministry of Manpower, Labour Market Report, second quarter 2026 (21 September 2026)"),
]


# Each post: slug, category, title, dek, description, outlook, figures, body, sources, related.
POSTS = []


def post(**kw):
    kw.setdefault("outlook", None)
    kw.setdefault("sources", SOURCES_MOM)
    POSTS.append(kw)


post(
    slug="market.html",
    category="Market review",
    title="Singapore's job market in the third quarter of 2026: more jobs, unevenly spread",
    card_title="Singapore's job market in Q3 2026: more jobs, unevenly spread",
    dek="Employment grew faster than in the spring, unemployment held at 2.0%, and hiring intentions recovered. Underneath, resident hiring was concentrated in a handful of sectors.",
    description="A review of Singapore's labour market in the third quarter of 2026: employment, unemployment, retrenchment, vacancies, and where resident hiring was concentrated.",
    figures=[("+27,700", "Total employment growth, third quarter 2026"), ("2.0%", "Overall unemployment, September 2026"), ("68,600", "Job vacancies in June 2026"), ("42.3%", "Firms expecting to hire, September poll")],
    body="""
<p>On the surface, the third quarter of 2026 was a good one for Singapore's labour market. Total employment, excluding migrant domestic workers, grew by 27,700 — well ahead of the 11,400 recorded in the second quarter and above the 25,100 of a year earlier. Unemployment was unchanged at 2.0% in September.</p>
<p>The detail tells a more nuanced story. Most of the increase was non-resident employment, mainly in construction and manufacturing. Resident employment also grew faster than in the previous quarter, but that growth was concentrated in a narrow band of sectors.</p>
<h2>Where resident hiring grew</h2>
<p>The Ministry of Manpower's advance release identified public administration and education, transportation and storage, and health and social services as the main sources of resident employment growth. These are sectors where full-time and shift-based part-time roles make up much of the hiring.</p>
<p>By contrast, resident employment growth in information and communications, financial services, and professional services was subdued. These outward-oriented sectors are also where hybrid, online, contract, and freelance arrangements are most commonly advertised, which is why the <a href="work-options.html">work types series</a> on this blog reads each arrangement against the sector it usually sits in.</p>
<blockquote class="pullquote">A rising national total and a quiet resident market in technology or finance can both be true in the same quarter.</blockquote>
<h2>Unemployment and retrenchment</h2>
<p>While the overall rate held at 2.0%, the resident unemployment rate edged up from 2.9% in August to 3.0% in September, and the citizen rate from 3.0% to 3.1%. Retrenchments rose from 4,620 in the second quarter to 4,800 in the third, though the incidence was unchanged at 2.0 per 1,000 employees. MOM said retrenchments remained elevated in selected outward-oriented sectors, with business reorganisation still the main reason.</p>
<p>The second-quarter report gives a clearer picture of where those job losses were. Retrenchments rose in manufacturing (from 670 to 870), information and communications (530 to 720), and financial services (560 to 710). Reorganisation or restructuring accounted for 72.1% of the total.</p>
<p>Re-entry has also slowed. Of residents retrenched in the second quarter, 54.9% were back in work within six months, down from 60.7% in the first quarter. The twelve-month figure was 69.8%. The resident long-term unemployment rate was 1.0% in June, up from 0.9% in March.</p>
<h2>Vacancies, as of June</h2>
<p>Job vacancies fell to 68,600 in June 2026, from 73,300 in March and 76,200 a year earlier, putting the vacancy rate at 2.8% and the ratio at 1.48 vacancies for every unemployed person. The sharpest declines were in financial services (5,800 to 4,500) and information and communications (5,300 to 4,400).</p>
<p>Entry-level PMET vacancies — professional, manager, executive, and technician roles advertised with a minimum salary between $2,300 and $5,000 — numbered 31,700, or 45.3% of the total. That salary band is the survey's definition of the group, not a benchmark for pay.</p>
<h2>What employers expect next</h2>
<p>Hiring sentiment improved in September. The share of firms expecting to hire over the next three months rose to 42.3% from 30.5% in August, and the share expecting to raise wages rose to 19.9% from 16.9%. The share expecting to retrench also edged up, from 2.8% to 3.1%. MOM noted that expectations remained below July's levels and that firms were staying selective.</p>
<h2>What to watch in December</h2>
<p>The full Labour Market Report for the third quarter, expected in mid-December 2026, will add sector-level employment, updated vacancy counts, turnover, and re-entry rates. Until then, the vacancy figures cited across this blog remain those for June.</p>
""",
    sources=SOURCES_MOM + [("https://stats.mom.gov.sg/publications/article-key-indicators-from-2q-2026/", "MOM Manpower Research and Statistics Department, key indicators from 2Q 2026")],
    related=["full-time-work.html", "industry-technology.html", "contract-work.html"],
)

post(
    slug="full-time-work.html",
    category="Work types",
    series=1,
    title="Full-time work in Singapore: where hiring is holding at the end of 2026",
    card_title="Full-time work: where hiring is holding",
    dek="Full-time employment remains the backbone of resident jobs. This year, which sectors are doing the hiring matters as much as how much hiring there is.",
    description="Where full-time hiring is holding in Singapore in late 2026, which sectors have become more selective, and how a full-time role is usually structured.",
    figures=[("+27,700", "Total employment growth, third quarter 2026"), ("4,500", "Financial services vacancies in June, from 5,800"), ("4,400", "Information and communications vacancies in June, from 5,300")],
    body="""
<p>Full-time work is still the dominant pattern in Singapore's resident workforce. What changed over 2026 is where that full-time hiring is happening. The latest Ministry of Manpower figures show steady demand in essential and public services, and a markedly more selective market in the sectors that drove much of the hiring in earlier years.</p>
<h2>Where full-time hiring is holding</h2>
<p>Resident employment growth in the third quarter of 2026 was led by public administration and education, transportation and storage, and health and social services. Many of the roles in these sectors are full-time positions, often built around rosters, schemes, or fixed recruitment windows rather than rolling advertisements.</p>
<p>That pattern matters for anyone reading the headline employment number. The 27,700 increase in total employment was mostly non-resident, concentrated in construction and manufacturing. The resident story sits in the sectors above.</p>
<h2>Where it has become more selective</h2>
<p>In financial services, information and communications, and professional services, resident employment growth was subdued in the third quarter. Vacancies had already fallen by June: from 5,800 to 4,500 in financial services, and from 5,300 to 4,400 in information and communications. Retrenchments in both sectors rose in the second quarter, with business reorganisation the main driver.</p>
<p>Full-time roles in these sectors have not disappeared, but the advertisements that remain tend to be more specific — naming a system, a regulation, or a measurable piece of work rather than a broad job family.</p>
<blockquote class="pullquote">Full-time work is still where most resident hiring happens. The difference this year is which sectors are doing it.</blockquote>
<h2>How a full-time role is usually structured</h2>
<p>A full-time position is a contract of service, typically built around a standard working week. The Employment Act sets the baseline for most employees, covering working hours, overtime, rest days, and leave. Probation, notice periods, and benefits are set out in the contract itself. For Singapore citizens and permanent residents, the employer contributes to CPF on wages above $50 a month, alongside the employee's share once wages pass $500.</p>
<h2>What full-time advertisements commonly state</h2>
<ul class="checks">
<li>The legal name of the employer and the work location.</li>
<li>Working hours, including shifts, weekends, or on-call arrangements where relevant.</li>
<li>The salary basis and, increasingly, a salary range.</li>
<li>Any registration, licence, or qualification the role depends on.</li>
</ul>
<h2>The outlook</h2>
<p>In MOM's September poll, 42.3% of firms said they expected to hire in the next three months, up from 30.5% in August, while remaining selective. The mid-December labour market report will show whether that improvement reached the sectors where full-time hiring has been quietest.</p>
""",
    related=["part-time-work.html", "market.html", "industry-public.html"],
)

post(
    slug="part-time-work.html",
    category="Work types",
    series=2,
    title="Part-time work in Singapore: hours, CPF, and the sectors still hiring",
    card_title="Part-time work: hours, CPF, and who is hiring",
    dek="Part-time work has a clear legal definition in Singapore, and in 2026 it is concentrated in the same sectors that are supporting resident employment.",
    description="How part-time work is defined under Singapore's Employment Act, how CPF applies, and where part-time hours are concentrated in late 2026.",
    figures=[("Under 35", "Contracted hours a week for a part-time employee"), ("$50", "Monthly wage above which CPF applies"), ("$500", "Monthly wage up to which only the employer share is paid")],
    body="""
<p>Part-time work is often discussed as a looser form of employment. In Singapore it is not. The Employment Act defines a part-time employee as someone contracted to work fewer than 35 hours a week — and that person is an employee in every other respect.</p>
<h2>What counts as part-time</h2>
<p>Because part-time staff are employees under a contract of service, the main protections follow from that status. Annual leave and other entitlements are generally pro-rated to the hours worked. For Singapore citizens and permanent residents, CPF applies once total wages exceed $50 a month. Where monthly wages are above $50 and no more than $500, only the employer's share is payable. Contributions fall due by the 14th of the following month, or the next working day.</p>
<p>CPF Board has also announced higher contribution rates for senior employees from 1 January 2027. The current rate tables are published on its website.</p>
<blockquote class="pullquote">A part-time employee is still an employee. That one fact settles most questions about leave and CPF.</blockquote>
<h2>Where part-time hours are concentrated</h2>
<p>Part-time work is most visible in care, transport and storage, and essential and public services. These are the same sectors the Ministry of Manpower identified as the main sources of resident employment growth in the third quarter of 2026, which makes part-time roles one of the steadier parts of the current market.</p>
<p>In care in particular, part-time positions are often shift-based and attached to a specific centre. In transport and storage, they are usually tied to a site, a shift pattern, and sometimes a licence class.</p>
<h2>Part-time work alongside a main job</h2>
<p>Some workers hold a part-time role alongside a full-time position. Whether that is possible depends on the hours, rest-day rules, and any outside-work clause in the existing contract. Pay from part-time work depends on the hours actually rostered, which can vary from week to week.</p>
<h2>What part-time advertisements commonly state</h2>
<ul class="checks">
<li>An hourly or monthly rate, and whether there is a minimum number of hours.</li>
<li>The shift pattern and how far ahead rosters are published.</li>
<li>The site or sites where the work takes place.</li>
<li>Whether the role is employment or a freelance engagement, which changes the CPF position.</li>
</ul>
""",
    sources=[("https://www.mom.gov.sg/employment-practices/part-time-employment", "Ministry of Manpower, part-time employment under the Employment Act"), ("https://www.cpf.gov.sg/employer/employer-obligations/how-much-cpf-contributions-to-pay", "CPF Board, CPF contribution rates for employers")] + SOURCES_MOM[:1],
    related=["full-time-work.html", "industry-care.html", "freelance-work.html"],
)

post(
    slug="hybrid-work.html",
    category="Work types",
    series=3,
    title="Hybrid work in Singapore: office-day arrangements in a selective market",
    card_title="Hybrid work in a selective market",
    dek="Hybrid has become standard language in technology and finance advertising. In 2026, that language sits in a market with fewer openings.",
    description="How hybrid work is usually arranged in Singapore, where it is most common, and how the Tripartite Guidelines on flexible work requests apply.",
    figures=[("1 Dec 2024", "Tripartite flexible-work request guidelines took effect"), ("2 months", "Time an employer has to respond to a formal request"), ("4,500", "Financial services vacancies in June, from 5,800")],
    body="""
<p>Few phrases appear more often in Singapore's technology and financial-services job advertisements than "hybrid working". The arrangement has outlasted the pandemic years and settled into a familiar pattern. What has changed in 2026 is the market around it.</p>
<h2>The market around hybrid roles</h2>
<p>The sectors where hybrid arrangements are most common are also the ones where hiring has tightened. Financial services vacancies fell from 5,800 in March to 4,500 in June, and information and communications from 5,300 to 4,400. Resident employment growth in both sectors, along with professional services, was subdued in the third quarter, and retrenchments rose in the second.</p>
<p>Hybrid roles are still being advertised. In a selective market, though, they tend to be more precise about expectations.</p>
<h2>What hybrid usually means in practice</h2>
<p>Most hybrid roles specify a number of office days a week, sometimes with fixed "anchor" days when a whole team is expected in. Others set core hours during which staff need to be reachable. The word "flexible" in an advertisement can mean hybrid days, but it can also refer to staggered hours or compressed weeks, so the details in the posting are the meaningful part.</p>
<blockquote class="pullquote">In a tighter market, hybrid advertisements are becoming more precise about office days, not less.</blockquote>
<h2>The formal request framework</h2>
<p>Since 1 December 2024, the Tripartite Guidelines on Flexible Work Arrangement Requests have set out how employees can make a formal request. The request is made in writing and covers the arrangement sought, the reason, and the intended start and end dates. Employers are expected to consider requests properly and respond within two months, and they may decline on reasonable business grounds.</p>
<p>The framework applies to people already in a job. For a new role, the arrangement on offer is the one described in the advertisement and the contract.</p>
<h2>What hybrid advertisements commonly state</h2>
<ul class="checks">
<li>The number of office days, and whether any are fixed.</li>
<li>Core hours or time-zone overlap for regional teams.</li>
<li>Equipment provided for work away from the office.</li>
<li>Whether the arrangement is part of the contract or a team practice.</li>
</ul>
""",
    sources=[("https://www.tal.sg/tafep/employment-practices/work-life-harmony/tripartite-guidelines-on-flexible-work-arrangement-requests", "TAFEP, Tripartite Guidelines on Flexible Work Arrangement Requests"), ("https://www.mom.gov.sg/employment-practices/good-work-practices/flexible-work-arrangements", "Ministry of Manpower, flexible work arrangements")] + SOURCES_MOM,
    related=["online-work.html", "industry-finance.html", "industry-technology.html"],
)

post(
    slug="online-work.html",
    category="Work types",
    series=4,
    title="Online work in Singapore: how remote roles are being advertised in 2026",
    card_title="Online work: how remote roles are advertised",
    dek="There is no official count of online jobs in Singapore. The closest guide is the sector data — and the warnings about online job scams.",
    description="How online and remote work is advertised in Singapore in late 2026, where it appears, and how it differs from hybrid work and from online job scams.",
    figures=[("4,400", "Information and communications vacancies in June, from 5,300"), ("720", "Information and communications retrenchments, second quarter"), ("1799", "ScamShield helpline")],
    body="""
<p>"Online work" covers a wide range of arrangements: fully remote employment with a Singapore company, contract roles for regional teams, and freelance projects delivered entirely over the internet. It is one of the most searched-for kinds of work, and one of the least clearly defined.</p>
<h2>No separate official count</h2>
<p>The Ministry of Manpower does not publish a count of online or remote jobs. The nearest indicator is the data for the sectors where such roles are most common. In information and communications, vacancies fell from 5,300 in March to 4,400 in June 2026, and retrenchments rose from 530 in the first quarter to 720 in the second. Resident employment growth in the sector was subdued in the third quarter.</p>
<p>Online roles continue to be advertised within that tighter market, mainly in software, data, design, and parts of professional services.</p>
<h2>Online, remote, and hybrid are not the same</h2>
<p>Many advertisements that describe a role as online still include overlap hours, occasional office days, or a requirement to be based in Singapore. Fully remote employment remains a minority arrangement. Freelance online work is different again: it is self-employment, with its own CPF and tax position.</p>
<blockquote class="pullquote">Most roles described as online still come with a location, a schedule, or both.</blockquote>
<h2>Where online work and job scams overlap</h2>
<p>Job scams remain among the most commonly reported scam types in Singapore, and many are framed as easy online work. A familiar pattern involves simple tasks — rating products, liking posts, or reviewing hotels — followed by a request to deposit money to "unlock" larger payments. Genuine employers do not ask workers to pay to start a job.</p>
<p>The Singapore Police Force and ScamShield publish current scam alerts, and the ScamShield helpline is 1799.</p>
<h2>What genuine online roles commonly state</h2>
<ul class="checks">
<li>A named employer or client, with a company website and registered business.</li>
<li>Working hours or overlap with a team's time zone.</li>
<li>Whether the role is employment, a contract, or freelance.</li>
<li>Payment terms that do not depend on the worker paying anything first.</li>
</ul>
""",
    sources=SOURCES_MOM + [("https://www.scamshield.gov.sg/", "ScamShield, scam alerts and helpline")],
    related=["hybrid-work.html", "freelance-work.html", "applying.html"],
)

post(
    slug="contract-work.html",
    category="Work types",
    series=5,
    title="Contract and project-based work in Singapore: reading the terms in a restructuring year",
    card_title="Contract and project work in a restructuring year",
    dek="Fixed-term and project-based roles are common in technology and professional services. With reorganisation driving most retrenchments, the terms of those contracts matter more.",
    description="How contract and project-based work is structured in Singapore, where it is common in late 2026, and which contract terms usually appear.",
    figures=[("72.1%", "Share of second-quarter retrenchments due to reorganisation"), ("31,700", "Entry-level PMET vacancies in June"), ("4,800", "Retrenchments in the third quarter")],
    body="""
<p>Contract work has long been a feature of Singapore's technology and professional-services sectors, where teams scale up for a system rollout, an audit cycle, or a client engagement. In 2026, it sits against a backdrop of restructuring: business reorganisation accounted for 72.1% of retrenchments in the second quarter.</p>
<h2>A restructuring year</h2>
<p>Professional services and information and communications both recorded resident employment gains in the second quarter, followed by subdued growth in the third. Retrenchments across the economy rose to 4,800 in the third quarter, with MOM noting they remained elevated in selected outward-oriented sectors. For firms uncertain about headcount, fixed-term and project-based arrangements are a common way to keep work moving.</p>
<h2>Fixed-term employment and project fees</h2>
<p>"Contract" covers two quite different arrangements. A fixed-term contract of service is employment: it ends on a set date, but Employment Act protections and CPF apply while it runs. A project fee paid under a contract for service is self-employment, with the worker responsible for their own CPF and tax position.</p>
<blockquote class="pullquote">"Contract" can mean employment with an end date or self-employment with a fee. The difference shapes CPF, leave, and tax.</blockquote>
<h2>Through an agency</h2>
<p>Many contract roles in technology and professional services are filled through staffing agencies. In that case the agency, not the client firm, is usually the employer of record — the party that pays salary and CPF. Licensed employment agencies can be checked on the Ministry of Manpower's Employment Agency Directory.</p>
<h2>What contract terms commonly cover</h2>
<ul class="checks">
<li>The employer of record and the client the work is for.</li>
<li>The start and end dates, and whether the project end is also the contract end.</li>
<li>Early termination, notice, and renewal terms.</li>
<li>Leave accrual and CPF, where the role is employment.</li>
</ul>
<h2>Entry-level professional roles</h2>
<p>Entry-level PMET vacancies stood at 31,700 in June, 45.3% of all vacancies, with professional services among the sectors represented. MOM defines the group as roles advertised with a minimum salary between $2,300 and $5,000. Some of those openings are fixed-term or project-based.</p>
""",
    sources=SOURCES_MOM + [("https://service2.mom.gov.sg/eadirectory/", "Ministry of Manpower, Employment Agency Directory")],
    related=["freelance-work.html", "industry-professional.html", "market.html"],
)

post(
    slug="freelance-work.html",
    category="Work types",
    series=6,
    title="Freelance work in Singapore: project work, CPF, and tax outside employment",
    card_title="Freelance work: project work outside employment",
    dek="Freelancing fits a market in which firms want defined pieces of work without adding headcount. It also comes with its own rules on CPF, tax, and contracts.",
    description="How freelance work fits Singapore's job market in late 2026, how self-employed CPF and tax apply, and what freelance agreements usually cover.",
    figures=[("1 Jan 2025", "Platform Workers Act took effect"), ("72.1%", "Share of second-quarter retrenchments due to reorganisation"), ("42.3%", "Firms expecting to hire, September poll")],
    body="""
<p>Freelance work in Singapore spans design, writing, software, consulting, tutoring, and a wide range of professional services. It is paid per project or per engagement, and it sits outside employment. In a year of selective hiring, it is one of the ways firms continue to get work done without adding permanent headcount.</p>
<h2>Freelancing in a selective market</h2>
<p>Technology, financial services, and professional services all saw subdued resident employment growth in the third quarter of 2026, after fewer vacancies and higher retrenchments earlier in the year. Those are also the sectors that commission much of Singapore's project-based freelance work. MOM's September poll showed hiring expectations improving but firms remaining selective.</p>
<h2>Self-employed status</h2>
<p>A freelancer works under a contract for service rather than a contract of service. Employment Act protections do not apply in the same way, and CPF and income tax follow the self-employed rules published by CPF Board and IRAS. Self-employed persons with annual net trade income above $6,000 make their own MediSave contributions, calculated after IRAS assesses their income.</p>
<p>Delivery and ride-hail workers on digital platforms are covered by a separate framework. The Platform Workers Act, in force since 1 January 2025, provides for CPF contributions and work injury compensation for that group.</p>
<blockquote class="pullquote">A job title that says "partner" or "associate" can be employment or freelance. The contract, not the title, decides.</blockquote>
<h2>Freelancing alongside a main job</h2>
<p>Some freelancers take on projects alongside a full-time or part-time role. Whether that is possible depends on the main contract, including any outside-work or conflict-of-interest clauses. Income from freelance work varies with the projects that come in, and this blog does not estimate earnings.</p>
<h2>What freelance agreements commonly cover</h2>
<p>The Tripartite Standard on Contracting with Self-Employed Persons sets out practices such as written agreements and timely payment. Agreements that follow it usually include:</p>
<ul class="checks">
<li>The scope of work and deliverables.</li>
<li>The fee, payment schedule, and invoicing terms.</li>
<li>Ownership of the work produced.</li>
<li>What happens if the project is cancelled or changed.</li>
</ul>
""",
    sources=[("https://www.cpf.gov.sg/member/growing-your-savings/cpf-contributions/saving-as-a-self-employed-person", "CPF Board, saving as a self-employed person"), ("https://www.iras.gov.sg/taxes/individual-income-tax/self-employed-and-partnerships", "IRAS, self-employed individuals and partnerships"), ("https://www.mom.gov.sg/employment-practices/platform-workers-act", "Ministry of Manpower, Platform Workers Act")] + SOURCES_MOM[:1],
    related=["contract-work.html", "online-work.html", "part-time-work.html"],
)


def industry_post(slug, title, card_title, dek, description, outlook, work_types, figures, situation, advertising, details, related):
    body = f"""
<p class="worktypes"><strong>Work types most often seen:</strong> {work_types}</p>
<h2>Where the sector stands</h2>
{situation}
<h2>How roles are usually advertised</h2>
{advertising}
<h2>Details commonly found in postings</h2>
<ul class="checks">{"".join(f"<li>{d}</li>" for d in details)}</ul>
"""
    post(slug=slug, category="Industry report", title=title, card_title=card_title, dek=dek, description=description, outlook=outlook, figures=figures, body=body, related=related)


industry_post(
    "industry-care.html",
    "Care and community jobs in Singapore: steady resident demand in late 2026",
    "Care and community: steady resident demand",
    "Health and social services remained one of the main sources of resident employment growth, with full-time and part-time shift work at the centre.",
    "Health and social services hiring in Singapore in late 2026: steady resident demand, shift-based full-time and part-time roles, and registration requirements.",
    ("steady", "Steady"),
    "full-time and part-time shift work",
    [("3 sectors", "Led resident employment growth in Q3, including health and social services"), ("31,700", "Entry-level PMET vacancies in June, spanning care among other sectors")],
    """
<p>In the third quarter of 2026, resident employment growth was led by public administration and education, transportation and storage, and health and social services. Care sits in that last group, which covers hospitals, clinics, eldercare, disability support, and community services.</p>
<p>The sector was not among those driving the rise in retrenchments in the second quarter; those increases were concentrated in manufacturing, information and communications, and financial services. In June, entry-level PMET vacancies — roles with an advertised minimum salary between $2,300 and $5,000 — spanned sectors that included health and social services.</p>
<p>Nursing, therapy, pharmacy, and social work are regulated professions with registration requirements. Support and administrative roles more often turn on shift patterns, language, and the centre where the work takes place.</p>
""",
    """
<p>Care advertisements typically state the workplace, the shift pattern, and whether the role is employment or a freelance engagement. Part-time care work under a contract of service is employment, with CPF applying for citizens and permanent residents once monthly wages exceed $50.</p>
<p>For regulated roles, the meaning of "registered" or "enrolled" is set by the relevant professional board. Descriptions commonly mention shift attendance, record-keeping, and work with families.</p>
""",
    ["Registration or enrolment requirements for regulated roles.", "Shift patterns, including nights and weekends, and how far ahead rosters are published.", "Whether the role is employment or freelance, and who pays CPF.", "The centre or centres where the work is based."],
    ["part-time-work.html", "full-time-work.html", "industry-public.html"],
)

industry_post(
    "industry-technology.html",
    "Technology jobs in Singapore: hiring continues, on tighter terms",
    "Technology: hiring continues, on tighter terms",
    "Information and communications vacancies fell by June and resident growth slowed in the third quarter. Hybrid, online, contract, and freelance roles remain part of the mix.",
    "Information and communications hiring in Singapore in late 2026: fewer vacancies, slower resident growth, and how hybrid, online, contract, and freelance roles are advertised.",
    ("cautious", "Cautious"),
    "hybrid, online, contract, and freelance",
    [("4,400", "Vacancies in June, from 5,300 in March"), ("720", "Retrenchments in the second quarter, from 530"), ("200+", "AI-related courses in SWDA's public catalogue")],
    """
<p>Resident employment growth in information and communications was subdued in the third quarter of 2026, alongside financial services and professional services. That marks a change from the second quarter, when the sector still recorded resident employment gains.</p>
<p>Vacancies fell from 5,300 in March to 4,400 in June, and retrenchments rose from 530 in the first quarter to 720 in the second. MOM linked higher recruitment and resignation rates in the sector to business restructuring and movement between firms rather than to broad-based expansion.</p>
<p>Advertisements for data, cloud, cybersecurity, and applied AI work continue to appear. In a restructuring year, they tend to describe a tool in the context of day-to-day work rather than a list of product names.</p>
""",
    """
<p>Openings are fewer than a year ago, and the advertisements that remain tend to name a system, the scale of the workload, and the outcome expected. Hybrid arrangements are common, and some roles are advertised as remote or on fixed-term contracts, though many technology roles remain office-based.</p>
<p>On 16 September 2026, the Skills and Workforce Development Agency published a public catalogue of more than 200 AI-related courses, with a time-limited tool subscription for eligible citizens who enrol and attend. It is a list of courses, not of jobs.</p>
""",
    ["The system or product the role works on.", "Whether the role is permanent, fixed-term, or a vendor placement, and who the employer of record is.", "Office days, time-zone overlap, and on-call expectations.", "No fees for equipment, starter kits, or training as a condition of being considered."],
    ["hybrid-work.html", "online-work.html", "contract-work.html"],
)

industry_post(
    "industry-finance.html",
    "Finance jobs in Singapore: fewer vacancies, more selective hiring",
    "Finance: fewer vacancies, more selective hiring",
    "Financial services recorded one of the two largest vacancy declines by June, and resident employment growth slowed in the third quarter.",
    "Financial services hiring in Singapore in late 2026: fewer vacancies, more restructuring, and how full-time and hybrid roles are being advertised.",
    ("cautious", "Cautious"),
    "full-time and hybrid",
    [("4,500", "Vacancies in June, from 5,800 in March"), ("710", "Retrenchments in the second quarter, from 560"), ("72.1%", "Share of retrenchments due to reorganisation")],
    """
<p>Financial services vacancies fell from 5,800 in March 2026 to 4,500 in June, one of the two largest sector declines in the quarter. Retrenchments in the sector rose from 560 in the first quarter to 710 in the second, with business reorganisation the main reason across the economy.</p>
<p>Resident employment growth in financial services was subdued in the third quarter, after resident gains in the second. Compared with 2025, the sector now shows fewer vacancies and leaner teams in some areas, with remaining roles filled more selectively.</p>
<p>Operations, compliance, risk, finance transformation, and client servicing remain the main areas of activity in advertisements.</p>
""",
    """
<p>Open roles often name a regulation, a product, or a process — reconciliations, case handling, vendor due diligence, management reporting. Hybrid arrangements are widespread, and the number of office days is usually stated. A role described as flexible may still be largely office-based.</p>
<p>Some client-facing and representative roles require a licence. The Monetary Authority of Singapore maintains public registers for those roles, and advertisements often state whether a licence is required or will be sponsored.</p>
""",
    ["The employer of record, including when a role is advertised through an agency.", "Licence or certification requirements, and who pays for them.", "Office days and expected availability.", "The pay structure: base salary, allowances, or commission."],
    ["hybrid-work.html", "full-time-work.html", "market.html"],
)

industry_post(
    "industry-professional.html",
    "Professional services jobs in Singapore: a cooler quarter after earlier gains",
    "Professional services: cooler after earlier gains",
    "Legal, accounting, consulting, and engineering services added resident jobs in the second quarter, then slowed in the third. Project-based contracts are a large part of the picture.",
    "Professional services hiring in Singapore in late 2026: resident gains in the second quarter, slower growth in the third, and the role of project-based contracts.",
    ("mixed", "Mixed"),
    "project-based contracts, hybrid, and some freelance",
    [("31,700", "Entry-level PMET vacancies in June"), ("45.3%", "Share of all vacancies that were entry-level PMET")],
    """
<p>Professional services recorded resident employment gains in the second quarter of 2026, along with other outward-oriented sectors. In the third quarter, resident growth in the sector was subdued, leaving a cooler picture than the second quarter alone suggested.</p>
<p>In June, entry-level PMET vacancies included professional services alongside health and social services. Those 31,700 vacancies covered roles advertised with a minimum salary between $2,300 and $5,000, a statistical grouping that spans many kinds of firms.</p>
<p>The sector covers legal, accounting, management consulting, architecture, and engineering. Conditions can differ sharply between practices, and advertisements in a specific field carry more information than the sector label.</p>
""",
    """
<p>Advertisements often refer to a specific piece of client work: an audit, a model, a set of drawings, a managed account. Titles such as "associate" vary in meaning from firm to firm. Project-based contracts are common, and the contract length, early-termination terms, and employer — the firm itself or a staffing company — shape the pay and CPF position.</p>
""",
    ["Whether the employer is the firm itself or an agency placing staff at the firm.", "Utilisation or billing targets, where mentioned.", "The qualification route for regulated work, as set by the professional body.", "Whether the end of a project also ends the employment."],
    ["contract-work.html", "freelance-work.html", "skills.html"],
)

industry_post(
    "industry-logistics.html",
    "Logistics, transport, and manufacturing jobs in Singapore: a split picture",
    "Logistics and industry: a split picture",
    "Transport and storage supported resident employment growth. Manufacturing's growth was mostly non-resident, alongside higher retrenchments.",
    "Logistics, transport, and manufacturing hiring in Singapore in late 2026: resident growth in transport and storage, non-resident growth in manufacturing.",
    ("mixed", "Mixed"),
    "full-time and part-time site and shift work",
    [("870", "Manufacturing retrenchments in Q2, from 670"), ("+27,700", "Total employment growth in Q3, mostly non-resident")],
    """
<p>Transportation and storage was one of the sectors supporting resident employment growth in the third quarter of 2026, alongside public administration and education and health and social services. That includes land transport, warehousing, and parts of the supply chain.</p>
<p>Manufacturing presents a different picture. Non-resident employment drove most of the economy's employment increase in the third quarter, mainly in construction and manufacturing. Manufacturing retrenchments rose from 670 to 870 in the second quarter. Construction's employment growth is largely work-permit hiring and does not translate directly into resident vacancies.</p>
<p>Vacancy figures for these sectors will be updated in the mid-December report.</p>
""",
    """
<p>In transport and warehousing, advertisements typically turn on licence class, shift pattern, and site. In manufacturing, production-operator roles and technician or engineer roles are advertised separately. With retrenchments higher here than in care or public services, contract length is often an important part of the posting.</p>
<p>Safety orientation and site access are standard parts of these roles. Requests to pay for a "site pass" before an employer has confirmed a role in writing fall outside ordinary hiring practice.</p>
""",
    ["The licence or certificate required.", "Shift hours, overtime practice, and the work site.", "Whether the role is employment, daily-rated, or freelance.", "Who issues any pass or permit, and whether any fee is involved."],
    ["full-time-work.html", "part-time-work.html", "market.html"],
)

industry_post(
    "industry-public.html",
    "Public and essential services jobs in Singapore: where resident growth is concentrated",
    "Public and essential services: where growth is concentrated",
    "Public administration and education led resident employment growth in the third quarter. Hiring here tends to follow schemes and recruitment windows.",
    "Public administration, education, and essential services hiring in Singapore in late 2026, and how scheme-based recruitment works.",
    ("steady", "Steady"),
    "full-time schemes, with some part-time",
    [("2.0%", "Overall unemployment, September 2026"), ("3.0%", "Resident unemployment, September 2026")],
    """
<p>The Ministry of Manpower's third-quarter advance release said resident employment growth continued to be supported mainly by essential and public services, naming public administration and education, transportation and storage, and health and social services. This report covers public administration and education; care and transport are covered separately.</p>
<p>Hiring in this sector often follows budget cycles, schemes, and fixed application windows rather than rolling advertisements. A quiet period on a job portal can simply reflect the gap between windows.</p>
<p>The second-quarter rise in retrenchments was concentrated in other sectors, and public administration and education were not among them.</p>
""",
    """
<p>Scheme details are typically published on the agency's own website or on Careers@Gov. Citizenship requirements, medical or security checks, and closing dates are commonly part of those listings.</p>
<p>Education roles may require a qualification, a registration, or both, and early-childhood and school roles fall under different schemes. Mid-career schemes sometimes recognise prior work experience and sometimes use a trainee pay point, which the advertisement specifies.</p>
""",
    ["The closing date and whether late applications are considered.", "Citizenship or residency requirements.", "Registration, medical, or security clearance requirements.", "The pay point for mid-career entrants, where published."],
    ["full-time-work.html", "industry-care.html", "skills.html"],
)

post(
    slug="applying.html",
    category="Practical guide",
    title="What a genuine job advertisement in Singapore usually includes",
    card_title="What a genuine job advertisement usually includes",
    dek="Whether the role is full-time, part-time, hybrid, online, contract, or freelance, legitimate postings share a common set of details. Some requests never belong in ordinary hiring.",
    description="What a genuine Singapore job advertisement usually contains, where applications are sent, and which requests fall outside ordinary hiring.",
    figures=[("1799", "ScamShield helpline"), ("1.48", "Vacancies per unemployed person, June 2026")],
    body="""
<p>Job advertisements in Singapore vary widely in length and style, but legitimate ones tend to share a core set of details. Knowing what those are makes it easier to compare roles — and to recognise the requests that do not belong in ordinary hiring.</p>
<h2>The market behind the advertisement</h2>
<p>The same application can meet very different conditions depending on the sector. In technology and finance, where vacancies fell and restructuring has been common, advertisements tend to be specific about systems and processes. In care and public services, where resident employment is still growing, they more often mention shifts, registration, or scheme windows. The <a href="industries.html">industry reports</a> on this blog cover each sector in more detail.</p>
<h2>What a legitimate posting usually contains</h2>
<ul class="checks">
<li>The legal name of the employer, not only a brand or a messaging-app group.</li>
<li>Whether the role is employment or freelance, along with the hours, workplace, and pay basis.</li>
<li>A closing date where relevant, and the documents requested.</li>
<li>No charge to apply, interview, or receive an offer.</li>
</ul>
<h2>Where applications are usually sent</h2>
<p>Most roles are listed on the employer's own careers page. MyCareersFuture, the government portal run by SWDA with GovTech, can be browsed without logging in; applying through it uses Singpass and is open to citizens and permanent residents. Reposts on other job boards can help with discovery, but the employer's own listing is the authoritative version.</p>
<h2>What a first application typically includes</h2>
<p>A first application is usually a CV and a short cover note. Personal identifiers — NRIC numbers, passport details, bank details, and dates of birth — are rarely needed at this stage. Employers who need a photograph generally say so in the advertisement.</p>
<blockquote class="pullquote">Ordinary employers do not charge candidates to apply, to interview, or to receive an offer.</blockquote>
<h2>Requests that fall outside ordinary hiring</h2>
<ul>
<li>A payment, a starter kit that must be purchased, or a cheque to be banked and partly returned.</li>
<li>A Singpass login, a one-time password, or a photograph of an NRIC in an early conversation.</li>
<li>Bank details requested before a written offer from an identifiable employer.</li>
<li>An interview conducted only through a personal messaging app, with no company email or published phone number.</li>
</ul>
<p>Suspected scams can be reported to the ScamShield helpline on 1799, and losses to the Singapore Police Force. ACRA's business-profile search shows whether a company is registered, though registration alone does not confirm that a job offer is genuine.</p>
""",
    sources=[("https://www.mycareersfuture.gov.sg/", "MyCareersFuture"), ("https://www.scamshield.gov.sg/", "ScamShield"), ("https://www.bizfile.gov.sg/", "ACRA Bizfile")],
    related=["online-work.html", "skills.html", "contract-work.html"],
)

post(
    slug="skills.html",
    category="Practical guide",
    title="SkillsFuture Credit at the end of 2026: amounts, the 1 December change, and the AI course list",
    card_title="SkillsFuture Credit in 2026: what changes on 1 December",
    dek="Credit amounts are unchanged, but the mid-career course list expands from 1 December, and SWDA has published a public catalogue of AI-related courses.",
    description="SkillsFuture Credit amounts in late 2026, the 1 December 2026 expansion of the mid-career course list, and SWDA's AI course catalogue.",
    figures=[("$500", "Opening SkillsFuture Credit, citizens aged 25 and above"), ("$4,000", "Mid-career credit, citizens aged 40 and above"), ("1 Dec 2026", "Mid-career course list expands")],
    body="""
<p>With hiring more selective in several sectors, advertisements increasingly name a specific skill, system, or registration. Singapore's public training credits are designed to sit alongside that kind of market, and two changes in the second half of 2026 are worth noting.</p>
<h2>The credit amounts</h2>
<p>Singapore citizens aged 25 and above receive an opening SkillsFuture Credit of $500, which can be used on courses listed on the MySkillsFuture portal and does not expire. Citizens aged 40 and above also receive a mid-career credit of $4,000 for selected courses, which likewise does not expire.</p>
<h2>What changes on 1 December 2026</h2>
<p>From 1 December 2026, new course runs of full Workforce Skills Qualifications and selected courses from sector agencies join the list of courses eligible for the mid-career credit. Balances and eligible courses are shown on MySkillsFuture after a Singpass login.</p>
<h2>A new agency and a new course list</h2>
<p>The Skills and Workforce Development Agency, formed from SkillsFuture Singapore and Workforce Singapore, began operating on 1 July 2026. On 16 September 2026 it published a public catalogue of more than 200 AI-related courses, with a time-limited tool subscription for eligible citizens who enrol and attend. The catalogue is a training list; completing a course and receiving a job offer are separate matters.</p>
<p>SkillsFuture Career Transition Programmes take a train-and-place approach for sectors with hiring demand. Places, sectors, and outcomes vary between runs, and each programme page explains what placement means for that intake.</p>
<blockquote class="pullquote">Credits are claimed through the official portal. No legitimate service asks for a Singpass login or a fee to unlock them.</blockquote>
<h2>Where the official information is published</h2>
<ul>
<li><a href="https://www.myskillsfuture.gov.sg/" rel="noopener">MySkillsFuture</a> for courses, credit balances, and subsidies.</li>
<li><a href="https://www.swda.gov.sg/" rel="noopener">Skills and Workforce Development Agency</a> for programmes and announcements.</li>
<li>Connect by SWDA at the Lifelong Learning Institute, a public centre for career and skills advice.</li>
<li><a href="https://www.mycareersfuture.gov.sg/" rel="noopener">MyCareersFuture</a>, the government career portal.</li>
</ul>
""",
    sources=[("https://www.myskillsfuture.gov.sg/", "MySkillsFuture, SkillsFuture Credit"), ("https://www.swda.gov.sg/", "Skills and Workforce Development Agency")],
    related=["industry-technology.html", "applying.html", "industry-professional.html"],
)

BY_SLUG = {p["slug"]: p for p in POSTS}
WORK_POSTS = sorted([p for p in POSTS if p["category"] == "Work types"], key=lambda p: p["series"])
INDUSTRY_POSTS = [p for p in POSTS if p["category"] == "Industry report"]
GUIDE_POSTS = [p for p in POSTS if p["category"] == "Practical guide"]


def meta_line(p) -> str:
    return f'<time datetime="{PUBLISHED_ISO}">{PUBLISHED}</time> · {reading_minutes(p["body"])} min read'


def card(p, featured=False) -> str:
    kicker = p["category"]
    if p.get("series"):
        kicker = f"Work types · Part {p['series']} of 6"
    pill = ""
    if p.get("outlook"):
        cls, label = p["outlook"]
        pill = f'<span class="pill {cls}">Outlook: {label}</span>'
    cls = "post-card featured" if featured else "post-card"
    title = p["title"] if featured else p["card_title"]
    return f'<a class="{cls}" href="{p["slug"]}"><span class="kicker">{kicker}</span>{pill}<h3>{title}</h3><p>{p["dek"]}</p><span class="meta">{meta_line(p)}</span></a>'


def render_post(p) -> str:
    hub_href, _ = CATEGORY_HUB[p["category"]]
    kicker = p["category"]
    if p.get("series"):
        kicker = f"Work types series · Part {p['series']} of 6"
    outlook = ""
    if p.get("outlook"):
        cls, label = p["outlook"]
        outlook = f'<span class="pill {cls}">Outlook: {label}</span>'
    sources = "".join(f'<li><a href="{u}" rel="noopener">{t}</a></li>' for u, t in p["sources"])
    series_nav = ""
    if p["category"] == "Work types":
        current_attr = ' aria-current="true"'
        items = "".join(
            f'<li{current_attr if w["slug"] == p["slug"] else ""}><a href="{w["slug"]}">{w["card_title"].split(":")[0]}</a></li>'
            for w in WORK_POSTS
        )
        series_nav = f'<div class="series"><h2>In this series</h2><ol>{items}</ol></div>'
    related = "".join(card(BY_SLUG[s]) for s in p["related"])
    return f"""
<article>
<header class="post-head"><div class="wrap narrow">
<p class="crumbs"><a href="index.html">Home</a><span>/</span><a href="{hub_href}">{p["category"]}</a></p>
<p class="eyebrow">{kicker}</p>
<h1>{p["title"]}</h1>
<p class="dek">{p["dek"]}</p>
<p class="byline"><span class="author">By {BYLINE}</span><span>{meta_line(p)}</span>{outlook}</p>
</div></header>
<div class="wrap post-grid">
<div class="prose">
{p["body"]}
<div class="sources-box"><h2>Sources</h2><ul>{sources}</ul></div>
<p class="post-note">Published {PUBLISHED}. Figures reflect the official releases available on that date; vacancy counts are for June 2026 until the third-quarter Labour Market Report is published in mid-December 2026. This article is general information and does not describe any specific vacancy.</p>
</div>
<aside class="post-aside">
{figbox(p["figures"])}
{series_nav}
</aside>
</div>
</article>
<section class="related"><div class="wrap">
<h2>Further reading</h2>
<div class="post-grid-cards">{related}</div>
</div></section>
"""


PAGES = {}

PAGES["index.html"] = (
    "home",
    "Full-time, part-time, hybrid, online, contract and freelance work in Singapore | WorkNest SG",
    "An independent Singapore blog on full-time, part-time, hybrid, online, contract, project-based, and freelance work, written from the latest official labour market figures.",
    f"""
<section class="masthead"><div class="wrap">
<p class="eyebrow">The WorkNest SG blog · Singapore · November 2026</p>
<h1><span>Full-time</span>, <span>part-time</span>, <span>hybrid</span>, <span>online</span>, <span>contract</span>, and <span>freelance</span> work.</h1>
<p class="dek">Reporting and analysis on how each kind of work is faring in Singapore's job market, drawn from the latest Ministry of Manpower figures.</p>
</div></section>

<section class="lead"><div class="wrap lead-grid">
{card(BY_SLUG["market.html"], featured=True)}
<aside class="snapshot" aria-label="The quarter in numbers">
<h2>The quarter in numbers</h2>
<div class="snap"><b>2.0%</b><span>Overall unemployment in September 2026, unchanged from August.</span></div>
<div class="snap"><b>+27,700</b><span>Total employment growth in the third quarter, mostly non-resident.</span></div>
<div class="snap"><b>42.3%</b><span>Firms expecting to hire in the next three months, up from 30.5%.</span></div>
<p class="src">Ministry of Manpower, Labour Market Advance Release, third quarter 2026.</p>
</aside>
</div></section>

<section class="alt"><div class="wrap">
<div class="section-head"><div><p class="eyebrow">Series</p><h2>Work types in Singapore</h2></div><a class="section-link" href="work-options.html">View the series</a></div>
<div class="post-grid-cards">{"".join(card(p) for p in WORK_POSTS)}</div>
</div></section>

<section><div class="wrap">
<div class="section-head"><div><p class="eyebrow">Industry reports</p><h2>How six sectors are hiring</h2></div><a class="section-link" href="industries.html">All industry reports</a></div>
<div class="post-grid-cards">{"".join(card(p) for p in INDUSTRY_POSTS)}</div>
</div></section>

<section class="alt"><div class="wrap">
<div class="section-head"><div><p class="eyebrow">Practical guides</p><h2>Applications and training</h2></div><a class="section-link" href="articles.html">All articles</a></div>
<div class="post-grid-cards two">{"".join(card(p) for p in GUIDE_POSTS)}</div>
</div></section>

<section><div class="wrap split">
<div>
<p class="eyebrow">Editorial approach</p>
<h2>Written from the official figures, and dated.</h2>
</div>
<div>
<p>Every article on WorkNest SG is based on published releases from the Ministry of Manpower and other public agencies, names its sources, and carries the date it was last reviewed. When a new labour market report changes the picture, the affected articles are revised and the change is recorded in the <a href="updates.html">editor's log</a>.</p>
<p>The next major release is MOM's Labour Market Report for the third quarter of 2026, expected in mid-December.</p>
<p><a href="about.html">About the blog</a></p>
</div>
</div></section>
""",
)

PAGES["work-options.html"] = (
    "work",
    "Work types in Singapore: full-time, part-time, hybrid, online, contract and freelance | WorkNest SG",
    "A six-part series on full-time, part-time, hybrid, online, contract and project-based, and freelance work in Singapore's job market in late 2026.",
    f"""
<header class="post-head"><div class="wrap">
<p class="eyebrow">Series · Six parts</p>
<h1>Work types in Singapore</h1>
<p class="dek">A six-part series on how full-time, part-time, hybrid, online, contract, and freelance work are faring in Singapore's job market at the end of 2026.</p>
</div></header>
<section class="tight"><div class="wrap">
<div class="tablewrap"><table>
<thead><tr><th>Work type</th><th>Where it is most visible</th><th>How it is usually structured</th></tr></thead>
<tbody>
<tr><td><a href="full-time-work.html">Full-time</a></td><td>Public services, care, and transport, where resident employment is growing.</td><td>Contract of service around a standard week, with leave, notice, and CPF.</td></tr>
<tr><td><a href="part-time-work.html">Part-time</a></td><td>Care, transport, and essential services.</td><td>Fewer than 35 contracted hours a week; still employment.</td></tr>
<tr><td><a href="hybrid-work.html">Hybrid</a></td><td>Technology and financial services.</td><td>A set number of office days, sometimes with fixed anchor days.</td></tr>
<tr><td><a href="online-work.html">Online</a></td><td>Technology, parts of professional services, and freelance projects.</td><td>Work delivered over the internet, often with overlap hours.</td></tr>
<tr><td><a href="contract-work.html">Contract and project-based</a></td><td>Technology and professional services.</td><td>Fixed-term employment, or a project fee under a contract for service.</td></tr>
<tr><td><a href="freelance-work.html">Freelance</a></td><td>Technology, finance, and professional services.</td><td>Self-employment, with CPF and tax under the self-employed rules.</td></tr>
</tbody>
</table></div>
<div class="post-grid-cards">{"".join(card(p) for p in WORK_POSTS)}</div>
</div></section>
""",
)

PAGES["industries.html"] = (
    "industries",
    "Industry reports: how Singapore's sectors are hiring | WorkNest SG",
    "Industry reports on care, technology, finance, professional services, logistics, and public services in Singapore, and the work types each sector advertises.",
    f"""
<header class="post-head"><div class="wrap">
<p class="eyebrow">Industry reports</p>
<h1>How six sectors are hiring</h1>
<p class="dek">Each report covers one sector's latest figures and the work arrangements most often advertised there, from full-time and part-time shift work to hybrid, contract, and freelance roles.</p>
</div></header>
<section class="tight"><div class="wrap">
<div class="post-grid-cards">{"".join(card(p) for p in INDUSTRY_POSTS)}</div>
<p class="hub-note">Outlook labels summarise the latest official data for each sector. See the <a href="market.html">quarterly market review</a> for the national picture.</p>
</div></section>
""",
)


def archive_group(title, posts):
    rows = "".join(
        f'<li><a href="{p["slug"]}">{p["title"]}</a><span class="meta">{meta_line(p)}</span></li>' for p in posts
    )
    return f"<h2>{title}</h2><ul class=\"archive\">{rows}</ul>"


PAGES["articles.html"] = (
    "articles",
    "All articles | WorkNest SG",
    "Every article on WorkNest SG: the quarterly market review, the work types series, industry reports, and practical guides.",
    f"""
<header class="post-head"><div class="wrap">
<p class="eyebrow">Archive</p>
<h1>All articles</h1>
<p class="dek">Every article published on WorkNest SG, grouped by section. All articles were last reviewed on {PUBLISHED}.</p>
</div></header>
<section class="tight"><div class="wrap narrow">
{archive_group("Market review", [BY_SLUG["market.html"]])}
{archive_group("Work types series", WORK_POSTS)}
{archive_group("Industry reports", INDUSTRY_POSTS)}
{archive_group("Practical guides", GUIDE_POSTS)}
</div></section>
""",
)

PAGES["updates.html"] = (
    "articles",
    "Editor's log | WorkNest SG",
    "A record of revisions to WorkNest SG articles and the official releases behind them.",
    """
<header class="post-head"><div class="wrap narrow">
<p class="eyebrow">Editor's log</p>
<h1>Revisions and the releases behind them</h1>
<p class="dek">Articles are revised when an official release changes the picture. Each entry records what changed and why.</p>
</div></header>
<section class="tight"><div class="wrap narrow">
<ul class="log">
<li><time datetime="2026-11-19">19 November 2026</time>
<p>Launch of the blog, including the quarterly market review, the six-part work types series, six industry reports, and two practical guides.</p>
<p>National employment, unemployment, retrenchment, and hiring-intention figures follow MOM's Labour Market Advance Release for the third quarter of 2026 (30 October 2026). Vacancy counts, the entry-level PMET definition, second-quarter retrenchment by sector, and re-entry rates follow the Labour Market Report for the second quarter of 2026 (21 September 2026).</p>
<p>SkillsFuture Credit amounts, the 1 December 2026 mid-career course change, SWDA's commencement on 1 July 2026, and the Tripartite Guidelines on flexible work requests are drawn from those agencies' public pages.</p>
<p>Next scheduled review: MOM's Labour Market Report for the third quarter of 2026, expected in mid-December 2026.</p>
</li>
</ul>
</div></section>
""",
)

PAGES["about.html"] = (
    "about",
    "About WorkNest SG",
    "WorkNest SG is an independent Singapore blog on work arrangements and the job market, written from official labour figures.",
    """
<header class="post-head"><div class="wrap narrow">
<p class="eyebrow">About</p>
<h1>About WorkNest SG</h1>
<p class="dek">An independent blog on how full-time, part-time, hybrid, online, contract, project-based, and freelance work are faring in Singapore's job market.</p>
</div></header>
<section class="tight"><div class="wrap split">
<div>
<h2>What we publish</h2>
<p>WorkNest SG publishes a quarterly review of Singapore's labour market, a series on the main work arrangements, reports on six industries, and practical guides on job advertisements and training credits. The aim is to set each kind of work against the latest official data, in plain and accurate language.</p>
<h2>Editorial standards</h2>
<p>Figures are taken from published releases by the Ministry of Manpower, CPF Board, the Skills and Workforce Development Agency, and other public bodies, and each article lists its sources. Articles carry the date they were last reviewed, and revisions are recorded in the <a href="updates.html">editor's log</a>. Corrections are welcome through the <a href="contact.html">contact page</a>.</p>
</div>
<div>
<h2>Independence</h2>
<p>WorkNest SG is independent of the Ministry of Manpower, the Skills and Workforce Development Agency, CPF Board, TAFEP, and any employer. It is not an employment agency.</p>
<ul>
<li>We do not list vacancies or recruit, screen, or place candidates.</li>
<li>We do not promise jobs, interviews, or levels of pay, and we do not estimate earnings.</li>
<li>We do not collect CVs, NRIC numbers, Singpass details, or payments.</li>
</ul>
<h2>Contact</h2>
<p>22 Orchard Road, #03-01, Singapore 238885<br>+65 8396 3756<br>support@worknestsg.com</p>
</div>
</div></section>
""",
)

PAGES["contact.html"] = (
    "contact",
    "Contact WorkNest SG",
    "Contact the WorkNest SG editorial team with corrections or topic suggestions. WorkNest SG does not accept job applications.",
    """
<header class="post-head"><div class="wrap narrow">
<p class="eyebrow">Contact</p>
<h1>Contact the editorial team</h1>
<p class="dek">We welcome corrections, updated figures, and suggestions for future articles. Job applications and CVs should be sent directly to employers; we are unable to forward them.</p>
</div></header>
<section class="tight"><div class="wrap split">
<div>
<p>Submitting the form opens a pre-addressed email in your own mail application, sent to support@worknestsg.com. Nothing is stored on this website, and no NRIC number, Singpass detail, or bank information is needed.</p>
<p>Phone: +65 8396 3756<br>22 Orchard Road, #03-01, Singapore 238885</p>
</div>
<div>
<form id="contact-form" class="form" novalidate>
<div class="field"><label for="name">Name</label><input id="name" name="name" autocomplete="name" required><div class="err" aria-live="polite"></div></div>
<div class="field"><label for="email">Email</label><input id="email" name="email" type="email" autocomplete="email" required><div class="err" aria-live="polite"></div></div>
<div class="field"><label for="topic">Topic</label><select id="topic" name="topic"><option>Correction to an article</option><option>Suggestion for a future article</option><option>General enquiry</option></select></div>
<div class="field"><label for="msg">Message</label><textarea id="msg" name="msg" required></textarea><div class="err" aria-live="polite"></div></div>
<button class="btn btn-primary" type="submit">Send message</button>
</form>
<div id="form-ok" class="ok" hidden tabindex="-1">
<h2>Thank you for getting in touch.</h2>
<p>Your email application should now be open with the message addressed to support@worknestsg.com. If it did not open, the same address can be used directly.</p>
</div>
</div>
</div></section>
""",
)

PAGES["disclaimer.html"] = (
    "about",
    "Disclaimer | WorkNest SG",
    "WorkNest SG publishes general information about Singapore's job market. No employment or income is promised.",
    """
<header class="post-head"><div class="wrap narrow">
<p class="eyebrow">Disclaimer</p>
<h1>Disclaimer</h1>
</div></header>
<section class="tight"><div class="wrap narrow prose">
<h2>General information</h2>
<p>WorkNest SG publishes general information about Singapore's labour market, industries, training, and work arrangements. It is not an employment agency. It does not publish vacancies and does not recruit, screen, place, or introduce candidates.</p>
<h2>No outcome is promised</h2>
<p>Nothing on this site promises an interview, a job, or any level of income. Hiring, pay, hours, and contract terms differ by employer and change over time. National statistics describe the market at the date cited and do not predict the outcome of any application.</p>
<h2>Not professional advice</h2>
<p>Articles are not legal, financial, or tax advice. Current rules on the Employment Act, CPF, flexible work, self-employment, and training credits are published by the Ministry of Manpower, CPF Board, IRAS, and the Skills and Workforce Development Agency.</p>
<h2>Sources and third parties</h2>
<p>We cite public sources and link to official websites. We do not control those sites, are not responsible for their content, and are not affiliated with them.</p>
<h2>Accuracy</h2>
<p>Each article is dated, and the <a href="updates.html">editor's log</a> records the release behind it. Corrections can be sent through the <a href="contact.html">contact page</a>.</p>
</div></section>
""",
)

PAGES["privacy.html"] = (
    "about",
    "Privacy Policy | WorkNest SG",
    "How WorkNest SG handles personal data under Singapore's Personal Data Protection Act 2012.",
    """
<header class="post-head"><div class="wrap narrow">
<p class="eyebrow">Privacy</p>
<h1>Privacy Policy</h1>
<p class="dek">Last updated: 19 November 2026</p>
</div></header>
<section class="tight"><div class="wrap narrow prose">
<p>WorkNest SG ("we", "us") handles personal data in line with Singapore's Personal Data Protection Act 2012 (PDPA). This policy explains what happens when you use this website.</p>
<h2>1. Who we are</h2>
<p>WorkNest SG is an independent publication about Singapore's job market. It is not an employment agency and does not collect CVs for placement.</p>
<h2>2. Personal data we collect</h2>
<p>The contact form does not send data to our server. It opens an email in your own mail application. A message may include your name, email address, and the content you choose to write. We do not ask for NRIC numbers, Singpass details, one-time passwords, bank details, or passwords.</p>
<h2>3. Technical data</h2>
<p>A web host may keep standard server logs, such as IP address, browser type, and pages requested, to keep the site secure and running. This site does not set advertising cookies and does not load third-party fonts or trackers.</p>
<h2>4. How we use personal data</h2>
<ul>
<li>To read and reply to corrections, questions, and suggestions.</li>
<li>To keep the website secure.</li>
<li>To meet legal requirements.</li>
</ul>
<p>We do not sell personal data and do not add anyone to a mailing list without separate consent.</p>
<h2>5. Disclosure</h2>
<p>We disclose personal data to an email service provider only as needed to receive and answer messages, where the law requires it, or with your consent.</p>
<h2>6. Transfers</h2>
<p>If a provider stores email outside Singapore, we take reasonable steps to ensure the data receives protection comparable to the PDPA.</p>
<h2>7. Protection and retention</h2>
<p>We take reasonable steps to protect the personal data we hold. Email is not perfectly secure. We keep messages only as long as needed to handle the enquiry or as required by law, then delete or anonymise them.</p>
<h2>8. Your rights</h2>
<p>You may request access to, or correction of, personal data we hold about you, or withdraw consent, by contacting our Data Protection Officer. We may need to verify your identity. If consent is withdrawn, we may be unable to continue handling the enquiry.</p>
<h2>9. Other websites</h2>
<p>Links to MOM, SWDA, CPF Board, MyCareersFuture, and other sites lead away from WorkNest SG. Their privacy practices are their own.</p>
<h2>10. Children</h2>
<p>This site is intended for a general audience and is not directed at children. If you believe a child has sent us personal data, please contact us and we will delete it.</p>
<h2>11. Changes</h2>
<p>The current version of this policy is the one on this page, with the date shown above.</p>
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
        write(name, title, description, current, body)
    for p in POSTS:
        _, current = CATEGORY_HUB[p["category"]]
        if p["slug"] == "market.html":
            current = "market"
        write(p["slug"], f'{p["title"]} | WorkNest SG', p["description"], current, render_post(p))
    favicon = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="9" fill="#1f5a4f"/><path d="M6 16.5 16 7l10 9.5" stroke="#f6f3ec" stroke-width="2.4" fill="none" stroke-linecap="round"/><path d="M9.5 15v9h13v-9" fill="#f6f3ec"/><circle cx="16" cy="19.5" r="2.4" fill="#c4553a"/></svg>"""
    (ROOT / "favicon.svg").write_text(favicon, encoding="utf-8")
    print(f"Wrote site to {ROOT}")


if __name__ == "__main__":
    main()
