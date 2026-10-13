"""Builds the static Fajar Foundation site into ./site (shared header/footer)."""
from pathlib import Path

OUT = Path(__file__).parent

EMAIL = "connects@fajarfoundation.org"
PHONE_DISPLAY = "+91 82081 86677"
PHONE_TEL = "+918208186677"
CIN = "U88900MH2024NPL418026"

PINWHEEL = '<img class="pinwheel-img" src="assets/img/pinwheel.png" alt="" width="44" height="44">'
LOGO = '<img class="logo-img" src="assets/img/logo-horizontal.png" alt="Fajar Foundation: Lighting the Way Forward" width="1200" height="416">'

NAV = [
    ("index.html", "Home", "home"),
    ("about.html", "About us", "about"),
    ("approach.html", "Our approach", "approach"),
    ("where-we-work.html", "Where we work", "where"),
    ("evidence.html", "Evidence", "evidence"),
    ("transparency.html", "Transparency", "transparency"),
    ("contact.html", "Contact", "contact"),
]

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta name="theme-color" content="#F5B700">
<link rel="icon" href="assets/img/favicon.png" type="image/png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Mukta:wght@400;500;600&family=Tiro+Devanagari+Marathi:ital@0;1&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<a class="pinwheel-fab" href="index.html" aria-label="Back to home page"><img src="assets/img/pinwheel.png" alt="" width="64" height="64"></a>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html" aria-label="Fajar Foundation home">
      {logo}
    </a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="site-nav">Menu</button>
    <nav class="nav" id="site-nav" aria-label="Main">
      <ul>
{nav}
        <li><a class="btn btn-primary" href="get-involved.html"{support_current}>Support our work</a></li>
      </ul>
    </nav>
  </div>
</header>
<main id="main">
"""

FOOT = """</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <div class="footer-brand">{pinwheel}<span>फजर · Fajar Foundation</span></div>
        <p>Career readiness for students in rural government schools, from Grade 8 onwards.</p>
      </div>
      <div>
        <h2>Visit or write</h2>
        <ul>
          <li>At Tawlar, Pathrot, Achalpur City,<br>Amravati - 444808, Maharashtra</li>
          <li><a href="mailto:{email}">{email}</a></li>
          <li><a href="tel:{tel}">{phone}</a></li>
        </ul>
      </div>
      <div>
        <h2>Pages</h2>
        <ul>
          <li><a href="about.html">About us</a></li>
          <li><a href="approach.html">Our approach</a></li>
          <li><a href="evidence.html">Evidence</a></li>
          <li><a href="get-involved.html">Support our work</a></li>
          <li><a href="transparency.html">Transparency</a></li>
        </ul>
      </div>
    </div>
    <div class="legal">
      <p>© <span id="year">2026</span> Fajar Foundation. A not-for-profit company registered under Section 8 of the Companies Act, 2013, in January 2024. CIN: {cin}</p>
    </div>
  </div>
</footer>
<script src="assets/js/main.js"></script>
</body>
</html>
"""


def page(filename, key, title, desc, body):
    nav_items = []
    for href, label, k in NAV:
        cur = ' aria-current="page"' if k == key else ""
        nav_items.append(f'        <li><a href="{href}"{cur}>{label}</a></li>')
    head = HEAD.format(
        title=title, desc=desc, logo=LOGO, nav="\n".join(nav_items),
        support_current=' aria-current="page"' if key == "involved" else "",
    )
    foot = FOOT.format(pinwheel=PINWHEEL, email=EMAIL, tel=PHONE_TEL, phone=PHONE_DISPLAY, cin=CIN)
    (OUT / filename).write_text(head + body + foot, encoding="utf-8")


ICONS = {
    "communication": '<path d="M4 5h16v11H9l-5 4z"/><path d="M8 9.5h8M8 12.5h5"/>',
    "teamwork": '<circle cx="8" cy="8" r="3"/><circle cx="17" cy="9" r="2.5"/><path d="M2.5 20c.4-3.3 2.8-5.5 5.5-5.5s5.1 2.2 5.5 5.5"/><path d="M14.5 15c.8-.6 1.6-.9 2.5-.9 2.3 0 4.1 1.8 4.5 4.9"/>',
    "creativity": '<path d="M9.5 18h5M10.5 21h3"/><path d="M12 3a6 6 0 0 0-3.9 10.6c.6.6.9 1.4.9 2.4h6c0-1 .3-1.8.9-2.4A6 6 0 0 0 12 3z"/>',
    "thinking": '<circle cx="10.5" cy="10.5" r="6"/><path d="M20 20l-5-5"/><path d="M8.5 9a2 2 0 1 1 2.8 1.8c-.5.3-.8.7-.8 1.2"/>',
    "problem": '<rect x="4" y="4" width="16" height="16" rx="2"/><path d="M8 12.5l2.8 2.8L16.5 9"/>',
    "planning": '<circle cx="6" cy="18" r="2"/><circle cx="18" cy="6" r="2"/><path d="M8 18h5.5a3 3 0 0 0 0-6h-3a3 3 0 0 1 0-6H16"/>',
    "tech": '<rect x="7" y="7" width="10" height="10" rx="1.5"/><path d="M10 3v4M14 3v4M10 17v4M14 17v4M3 10h4M3 14h4M17 10h4M17 14h4"/>',
}


def skill(icon, name, text):
    return f'<li><svg viewBox="0 0 24 24" aria-hidden="true">{ICONS[icon]}</svg><div><strong>{name}</strong><span>{text}</span></div></li>'


SKILLS = "\n".join([
    skill("communication", "Communication", "Speaking up in class, in interviews and with people outside the village."),
    skill("teamwork", "Teamwork", "Working with peers on real projects, sharing roles and settling disagreements."),
    skill("creativity", "Creativity", "Coming up with more than one way to approach a problem."),
    skill("thinking", "Critical thinking", "Asking why, weighing options and backing an opinion with reasons."),
    skill("problem", "Problem-solving", "Breaking a challenge into steps and trying again when the first attempt fails."),
    skill("planning", "Planning", "Setting a goal, mapping the route to it and tracking progress."),
    skill("tech", "IT &amp; AI skills", "Using a computer, the internet and AI tools safely and with purpose."),
])

HERO_ART = '''<img class="hero-bg" src="assets/img/hero1.jpg" width="1200" height="900" alt="Students in a rural classroom exploring career cards together" fetchpriority="high">
  <img class="hero-pinwheel" src="assets/img/pinwheel.png" alt="" width="120" height="120">'''

def person(slug, initials, name, role, teaser, more):
    return f"""<article class="person reveal">
  <div class="photo"><span class="initials" aria-hidden="true">{initials}</span><img src="assets/img/team/{slug}.jpg" alt="Portrait of {name}" loading="lazy"></div>
  <div class="person-body">
    <h3>{name}</h3><p class="role">{role}</p>
    <p class="teaser">{teaser}</p>
    <div class="more" id="bio-{slug}"><div><p>{more}</p></div></div>
    <button class="more-btn" type="button" aria-expanded="false" aria-controls="bio-{slug}" hidden>Read more</button>
  </div>
</article>"""


TEAM = chr(10).join([
    person("alim", "AS", "Alim Shaikh", "Co-Founder",
           "Alim studied in a rural school, and that experience shapes everything he does.",
           "Over seven years he has worked in education, youth development and public systems. He is a Gandhi Fellowship alumnus and has partnered with governments and communities to improve learning and to make programmes work on the ground. At Fajar he builds solutions that can grow, and that strengthen the local education systems students depend on."),
    person("kartik", "KC", "Kartik Chitrakar", "Co-Founder",
           "Kartik’s path into development began in Melghat, where Fajar works today.",
           "For more than ten years he has worked with rural communities, most of all in Chhattisgarh, on livelihoods, gender and youth development. He also mentors rural students who are aiming for higher education. At Fajar he works to open clear pathways for young people to step into their futures."),
    person("nitin", "NI", "Nitin Ingle", "Internal Governance Head",
           "Nitin has spent four years working alongside tribal communities in central India.",
           "His work spans climate resilience, rural governance and strengthening grassroots institutions. He has supported women farmers and community groups to build sustainable livelihoods and reach social protection. At Fajar he brings that field experience to community-led work."),
])

# ---------------------------------------------------------------- Home
HOME = f"""
<section class="hero">
  {HERO_ART}
  <div class="wrap">
    <div class="hero-copy">
      <h1>Rural students deserve to choose their future, not stumble into it.</h1>
      <p class="lead">Fajar Foundation works in rural government schools from Grade 8 onwards. We help students discover careers, build the skills to pursue them, and we stay with them after school.</p>
      <div class="actions">
        <a class="btn btn-primary" href="get-involved.html">Support our work</a>
        <a class="btn btn-ghost" href="approach.html">See how we work</a>
      </div>
    </div>
  </div>
</section>

<section class="night section" aria-labelledby="problem-h">
  <div class="wrap">
    <h2 id="problem-h">Before dawn: how career choices get made today</h2>
    <p class="vignette">SSC results are out at an ashram school in Melghat. A sixteen-year-old has a few weeks to choose Science, Commerce or Arts. She can name five jobs. No one she knows has done the one she half-wants. She picks what her friends pick.</p>
    <p class="small">A composite story, drawn from what we see in our schools.</p>
    <ul class="ledger">
      <li><span class="figure">4 in 10</span><p>rural young people aged 14 to 18 had no role model in the profession they hoped to join.<span class="src">ASER 2017 “Beyond Basics”, 28,323 rural youth</span></p></li>
      <li><span class="figure">19.9%</span><p>of Scheduled Tribe students in Maharashtra drop out during Classes 9 and 10, against 11.5% of all students.<span class="src">UDISE+ 2024-25, Ministry of Education</span></p></li>
      <li><span class="figure">1 in 5</span><p>students in Maharashtra do not move on from Class 10 to Class 11.<span class="src">UDISE+ 2024-25: transition rate 79.2%</span></p></li>
      <li><span class="figure">65.7%</span><p>of India’s unemployed youth had secondary education or more in 2022, up from 35.2% in 2000. Finishing school is no longer enough.<span class="src">ILO &amp; Institute for Human Development, India Employment Report 2024</span></p></li>
    </ul>
    <p class="small" style="margin-top:1.5rem">These students are not short of talent. They are short of exposure, role models, guidance and confidence in unfamiliar settings. <a href="evidence.html">Read the evidence</a></p>
  </div>
</section>
<div class="dawn-fade" aria-hidden="true"></div>

<section class="section band" aria-labelledby="work-h">
  <div class="wrap">
    <h2 id="work-h">What we do</h2>
    <p class="lead">We start early, before the big decisions, and we don’t leave when school ends.</p>
    <ol class="journey">
      <li><span class="when">Grades 8 to 10</span><h3>Discover</h3><p>Students learn about themselves and the world of work: their interests and strengths, the careers that exist, and the routes into them. They meet working professionals and practise making decisions.</p></li>
      <li><span class="when">Throughout</span><h3>Build</h3><p>Every career activity is designed to build transferable skills: speaking up, working in teams, thinking things through, planning ahead and using technology well.</p></li>
      <li><span class="when">After Class 10 and 12</span><h3>Bridge</h3><p>We help students with admissions and entrance exams, mentor them as they settle into college or work, and track how they grow over the years.</p></li>
    </ol>
  </div>
</section>

<section class="section" aria-labelledby="skills-h">
  <div class="wrap">
    <h2 id="skills-h">Skills that travel with them</h2>
    <p class="lead">Rural students can communicate well at home and in the village. What they often lack is practice and confidence in formal settings: a college seminar, a group project, a job interview. We build that through repeated, supported practice.</p>
    <ul class="skills">
{SKILLS}
    </ul>
    <p class="small" style="margin-top:1.25rem">Underneath all of these is agency: the confidence to make a decision about your own life and plan for it.</p>
  </div>
</section>

<section class="section band-ink now" aria-labelledby="now-h">
  <img class="now-mark" src="assets/img/pinwheel.png" alt="" width="420" height="420">
  <div class="wrap split">
    <div class="reveal">
      <span class="eyebrow">Where we are today</span>
      <h2 id="now-h">Small, honest, and just getting started.</h2>
      <p>We are a young organisation and we say so plainly. Today we work in two government tribal residential schools in Melghat, Amravati district. The work is unfunded so far.</p>
      <p>Next, we want to bring the programme to more schools and reach more students across rural Maharashtra.</p>
      <div class="actions"><a class="btn btn-primary" href="where-we-work.html">See where we work</a></div>
    </div>
    <div class="now-stats">
      <div class="stat-card reveal" style="--d:100ms"><b data-count="2">2</b><span>schools in Melghat</span></div>
      <div class="stat-card reveal" style="--d:220ms"><b data-count="183">183</b><span>students, Classes 9 to 12</span></div>
      <div class="stat-card stat-next reveal" style="--d:340ms"><b aria-hidden="true">+</b><span>More schools. More students.<br>That is where we are heading.</span></div>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="trust-h">
  <div class="wrap">
    <h2 id="trust-h">Why you can trust us</h2>
    <p>We are a not-for-profit company registered under Section 8 of the Companies Act, 2013. Our registration details, governance and status of tax registrations are all on one page.</p>
    <p>We measure what we do, and we will publish what we find, whether the results are good, mixed or disappointing.</p>
    <div class="actions"><a class="btn btn-ghost" href="transparency.html">View our registration details</a></div>
  </div>
</section>

<section class="section band" id="team" aria-labelledby="team-h">
  <div class="wrap">
    <span class="eyebrow">Our team</span>
    <h2 id="team-h">The people behind Fajar</h2>
    <p class="lead">Fajar is run by its founders, who give their evenings, weekends and alternate weeks to the schools we work with.</p>
    <div class="team">
      {TEAM}
    </div>
  </div>
</section>

<section class="section band" aria-labelledby="cta-h">
  <div class="wrap">
    <h2 id="cta-h">Help us reach more students</h2>
    <p class="lead">You can fund a school, mentor a student, speak about your career, or partner with us as an institution.</p>
    <div class="actions">
      <a class="btn btn-primary" href="get-involved.html">Support our work</a>
      <a class="btn btn-ghost" href="contact.html">Talk to us</a>
    </div>
  </div>
</section>
"""

# ---------------------------------------------------------------- About
ABOUT = f"""
<section class="page-hero"><div class="wrap">
  <h1>Fajar means dawn. We started because too many students reach adulthood in the dark about their options.</h1>
</div></section>

<section class="section"><div class="wrap split">
  <div>
    <h2>Why we exist</h2>
    <p>In rural government schools, the decisions that shape a young person’s life — which stream to take, whether to continue after Class 10, what to study next — are often made by marks, family pressure or what friends are doing. Few students have met someone who does the work they dream of. Few schools have a career counsellor.</p>
    <p>We believe a student from a village school should make these choices with as much information and confidence as a student anywhere else.</p>
  </div>
  <div>
    <h2>What we stand for</h2>
    <ul class="plain-list">
      <li><b>Students decide.</b> We don’t tell students what to become. We help them find out, think it through and decide.</li>
      <li><b>Start early, stay long.</b> We begin in Grade 8 and stay in touch after students leave school.</li>
      <li><b>Evidence over claims.</b> We measure our work carefully and share the results honestly.</li>
      <li><b>Rooted locally.</b> We work in the districts we come from, in the language students speak.</li>
    </ul>
  </div>
</div></section>

<section class="section band"><div class="wrap split">
  <div><h2>Our mission</h2><p class="lead">To prepare students in rural government schools to make informed career decisions and pursue them with confidence.</p></div>
  <div><h2>Our vision</h2><p class="lead">A rural India where every student’s future is shaped by their own informed choice, not by chance.</p></div>
</div></section>

<section class="section" id="team"><div class="wrap">
  <h2>Our team</h2>
  <p class="lead">Fajar is run by its founders, who give their evenings, weekends and alternate weeks to the schools we work with.</p>
  <div class="team">
    {TEAM}
  </div>
</div></section>
"""

# ---------------------------------------------------------------- Approach
STAGE_ICONS = {
    "discover": '''<svg class="ico ico-discover" viewBox="0 0 64 64" aria-hidden="true"><circle cx="32" cy="32" r="24"/><path class="tick" d="M32 8v5M32 51v5M8 32h5M51 32h5"/><g class="needle"><path d="M42 22 36 36 22 42 28 28Z"/></g><circle class="pin" cx="32" cy="32" r="2.2"/></svg>''',
    "build": '''<svg class="ico ico-build" viewBox="0 0 64 64" aria-hidden="true"><rect class="b b1" x="8" y="40" width="14" height="16" rx="2"/><rect class="b b2" x="25" y="28" width="14" height="28" rx="2"/><rect class="b b3" x="42" y="14" width="14" height="42" rx="2"/><path class="spark" d="M12 22l4-4M16 14v-5M7 17H2"/></svg>''',
    "bridge": '''<svg class="ico ico-bridge" viewBox="0 0 64 64" aria-hidden="true"><path class="deck" d="M4 40h56"/><path class="arch" d="M10 40c4-18 40-18 44 0"/><path class="hang" d="M20 40v-8M28 40V28M36 40V28M44 40v-8"/><path class="water" d="M6 50c4-3 8 3 13 0s9 3 13 0 9 3 13 0 8 3 13 0"/></svg>''',
}

MEASURE_ICONS = {
    "aware": '''<svg class="ico" viewBox="0 0 64 64" aria-hidden="true"><circle cx="32" cy="32" r="22"/><circle class="draw" cx="32" cy="32" r="13"/><circle class="pin" cx="32" cy="32" r="3.5"/></svg>''',
    "skills": '''<svg class="ico" viewBox="0 0 64 64" aria-hidden="true"><path d="M4 32s10-18 28-18 28 18 28 18-10 18-28 18S4 32 4 32Z"/><circle class="draw" cx="32" cy="32" r="8"/><circle class="pin" cx="32" cy="32" r="3"/></svg>''',
    "paths": '''<svg class="ico" viewBox="0 0 64 64" aria-hidden="true"><circle cx="14" cy="50" r="4"/><circle cx="50" cy="14" r="4"/><path class="draw" d="M18 50h18a10 10 0 0 0 0-20h-8a10 10 0 0 1 0-20h18"/></svg>''',
}


def stage(n, key, when, name, lead, items):
    lis = "".join(f"<li>{i}</li>" for i in items)
    return f'''<article class="stage reveal" style="--d:{n * 110}ms">
      <div class="stage-top"><div class="icon-tile">{STAGE_ICONS[key]}</div><span class="stage-no">0{n}</span></div>
      <span class="pill">{when}</span>
      <h3>{name}</h3>
      <p>{lead}</p>
      <ul class="ticks">{lis}</ul>
    </article>'''


def measure(n, key, name, text):
    return f'''<article class="measure-card reveal" style="--d:{n * 110}ms">
      <div class="icon-tile sm">{MEASURE_ICONS[key]}</div>
      <h3>{name}</h3><p>{text}</p>
    </article>'''


APPROACH = f"""
<section class="page-hero approach-hero">
  <img class="hero-watermark" src="assets/img/pinwheel.png" alt="" width="520" height="520">
  <div class="wrap">
    <span class="eyebrow">Our approach</span>
    <h1>We help students find out who they are, what’s possible and how to get there.</h1>
    <p class="lead">One programme, three stages. It starts in Grade 8, runs alongside school, and carries on after it.</p>
    <div class="chips" aria-label="Jump to a stage">
      <a href="#stages">Discover</a><span aria-hidden="true">→</span><a href="#stages">Build</a><span aria-hidden="true">→</span><a href="#stages">Bridge</a>
    </div>
  </div>
</section>

<section class="section" id="stages"><div class="wrap">
  <span class="eyebrow">How it works</span>
  <h2>Three stages, one student</h2>
  <div class="stages">
    {stage(1, "discover", "Grades 8 to 10", "Discover",
           "Weekly sessions take students from self-discovery to career knowledge to planning.",
           ["Activities to identify interests and strengths", "Exploring careers beyond the familiar handful",
            "Conversations with local working professionals", "Practice in weighing options before the stream choice after Class 10"])}
    {stage(2, "build", "Throughout", "Build",
           "Skills workshops, then practice inside every career activity, so students see why the skills matter.",
           ["Group discussions and presentations", "Team projects with real roles",
            "Hands-on computer, internet and AI use", "Planning and goal-setting exercises"])}
    {stage(3, "bridge", "After school", "Bridge",
           "Support at the moments when students are most likely to drift.",
           ["Guidance on courses, colleges and admissions", "Entrance exam preparation support",
            "Mentoring through the first years of college or work", "Tracking each student’s progress over time"])}
  </div>
</div></section>

<section class="section band"><div class="wrap">
  <span class="eyebrow">What we build</span>
  <h2>The skills we build</h2>
  <p class="lead">Practised again and again, inside every activity, until they feel ordinary.</p>
  <ul class="skills">
{SKILLS}
  </ul>
</div></section>

<section class="section"><div class="wrap">
  <span class="eyebrow">How we measure</span>
  <h2>We record a baseline, then follow the same students over time.</h2>
  <p class="lead">Three things tell us whether the programme is working:</p>
  <div class="measure-grid">
    {measure(1, "aware", "Career awareness and confidence", "How many careers and pathways a student can describe, and how sure they feel about deciding.")}
    {measure(2, "skills", "Skills, observed", "Concrete behaviours, such as whether a student asks questions, explains their reasoning or contributes in a group.")}
    {measure(3, "paths", "What students actually do", "The stream and course they choose, whether it matches their interests, and where they are a year later.")}
  </div>
</div></section>

<section class="section"><div class="wrap">
  <h2>Bring Fajar to your school</h2>
  <p class="lead">Teachers, headteachers and local organisations: we would like to hear from you.</p>
  <div class="actions"><a class="btn btn-primary" href="contact.html">Talk to us</a><a class="btn btn-ghost" href="where-we-work.html">Where we work</a></div>
</div></section>
"""

# ---------------------------------------------------------------- Where we work
WHERE = """
<section class="page-hero"><div class="wrap">
  <h1>We work where we come from: rural Maharashtra.</h1>
</div></section>

<section class="section"><div class="wrap split">
  <div>
    <h2>Now: Melghat, Amravati district</h2>
    <p>Melghat is a forested, largely tribal region in the Satpura hills of northern Amravati district. We work in two government tribal residential (ashram) schools here, with students in Classes 9 to 12.</p>
    <div class="facts">
      <div><b>2</b><span>schools</span></div>
      <div><b>183</b><span>students</span></div>
      <div><b>9–12</b><span>classes</span></div>
    </div>
    <p>In Maharashtra, Scheduled Tribe students drop out of Classes 9 and 10 at almost twice the overall rate. That is why we started here.</p>
    <p>Our office is at Tawlar, Pathrot, Achalpur City, Amravati - 444808, Maharashtra.</p>
  </div>
  <div>
    <iframe class="map" title="Map of Achalpur and Melghat, Amravati district" loading="lazy"
      src="https://www.openstreetmap.org/export/embed.html?bbox=76.95%2C21.15%2C77.85%2C21.70&amp;layer=mapnik"></iframe>
    <p class="small">Achalpur tahsil and the Melghat region, Amravati district. Map © OpenStreetMap contributors.</p>
  </div>
</div></section>

<section class="section band"><div class="wrap split">
  <div>
    <h2>Next: Beed district</h2>
    <p>We plan to extend the programme to schools in Beed district in Marathwada, where many students face the same lack of guidance at the same decision points.</p>
  </div>
  <div>
    <h2>How we work with schools</h2>
    <p>We work inside government schools, with the permission and support of school leadership and education officials. Sessions run during school time, and we involve teachers so the work can continue.</p>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <h2>Want Fajar in your school or district?</h2>
  <p class="lead">If you are a headteacher, education officer or local organisation in rural Maharashtra, we would like to hear from you.</p>
  <div class="actions"><a class="btn btn-primary" href="contact.html">Contact us</a></div>
</div></section>
"""

# ---------------------------------------------------------------- Evidence
def fact(n, figure, text, src):
    return f'''<li class="fact reveal" style="--d:{(n % 3) * 110}ms">
      <span class="figure">{figure}</span>
      <p>{text}</p>
      <span class="src">{src}</span>
    </li>'''


TOC_ICONS = {
    "start": '''<svg class="ico ico-fog" viewBox="0 0 64 64" aria-hidden="true"><circle cx="32" cy="32" r="22"/><path class="q" d="M25 26a7 7 0 1 1 10 6c-2 1.2-3 2.6-3 5"/><circle class="pin" cx="32" cy="45" r="1.6"/></svg>''',
    "early": '''<svg class="ico ico-spark" viewBox="0 0 64 64" aria-hidden="true"><path d="M24 44h16M27 52h10"/><path class="bulb" d="M32 8a15 15 0 0 0-9.5 26.6c1.7 1.4 2.5 3.4 2.5 5.4h14c0-2 .8-4 2.5-5.4A15 15 0 0 0 32 8Z"/><path class="rays" d="M6 22h5M53 22h5M12 8l4 4M52 8l-4 4"/></svg>''',
    "decide": '''<svg class="ico ico-fork" viewBox="0 0 64 64" aria-hidden="true"><path d="M32 56V34"/><path class="p1" d="M32 34 14 16"/><path class="p2" d="M32 34 50 16"/><path class="a1" d="M14 26V16h10"/><path class="a2" d="M40 16h10v10"/></svg>''',
    "hold": '''<svg class="ico ico-flag" viewBox="0 0 64 64" aria-hidden="true"><path d="M16 58V8"/><path class="flag" d="M16 10h32l-7 11 7 11H16"/><path d="M8 58h24"/></svg>''',
}


def toc_step(n, key, stage, title, text, doing, measure):
    chips = "".join(f'<span class="mini-chip">{d}</span>' for d in doing)
    return f'''<li class="reveal-step">
      <div class="step-card">
        <div class="step-head"><div class="icon-tile">{TOC_ICONS[key]}</div><span class="pill">{stage}</span></div>
        <h3>{title}</h3>
        <p>{text}</p>
        <dl>
          <dt>What we do</dt><dd>{chips}</dd>
          <dt>What we measure</dt><dd class="measure">{measure}</dd>
        </dl>
      </div>
    </li>'''


def question(n, text, why):
    return f'''<article class="q-card reveal" style="--d:{n * 110}ms">
      <span class="q-mark" aria-hidden="true">?</span>
      <h3>{text}</h3>
      <p>{why}</p>
    </article>'''


EVIDENCE = f"""
<section class="page-hero approach-hero">
  <img class="hero-watermark" src="assets/img/pinwheel.png" alt="" width="520" height="520">
  <div class="wrap">
    <span class="eyebrow">Evidence</span>
    <h1>What we know, what we don’t, and what we are testing.</h1>
    <p class="lead">We use national, published data, name every source, and say plainly where the evidence runs out.</p>
    <div class="chips" aria-label="On this page">
      <a href="#numbers">The numbers</a><span aria-hidden="true">→</span><a href="#theory">Theory of change</a><span aria-hidden="true">→</span><a href="#testing">What we’re testing</a>
    </div>
  </div>
</section>

<section class="section" id="numbers"><div class="wrap">
  <span class="eyebrow">The problem, in numbers</span>
  <h2>Students are leaving school without a plan.</h2>
  <p class="lead">Every figure below comes from a published national source.</p>
  <ul class="facts-grid">
    {fact(0, "40%", "of rural youth aged 14–18 had no role model in their hoped-for profession. Aspirations were also strongly gendered: young men chose the army, police or engineering; young women, teaching or nursing.", "ASER Centre, ASER 2017 “Beyond Basics” (28,323 youth, 26 districts, 24 states)")}
    {fact(1, "5.6%", "of rural youth aged 14–18 were taking any vocational training. Among those in Class 11 or above, 55.7% were in the Arts stream.", 'ASER Centre, <a href="https://asercentre.org/wp-content/uploads/2022/12/ASER-2023-Main-Findings_Jan-16-2024-1.pdf">ASER 2023 “Beyond Basics”</a> (34,745 youth, 28 districts)')}
    {fact(2, "32.6%", "of 18-year-olds in rural India are not enrolled in any education, compared with 3.9% of 14-year-olds.", "ASER 2023 “Beyond Basics”")}
    {fact(3, "19.9%", "secondary dropout rate for Scheduled Tribe students in Maharashtra, against 11.5% for all students.", 'UDISE+ 2024-25, <a href="https://www.education.gov.in/sites/upload_files/mhrd/files/parliament_annexure_en/LSUQ_5964.pdf">Ministry of Education, Lok Sabha reply</a>')}
    {fact(4, "79.2%", "of Maharashtra students move from Class 10 to Class 11; 75.1% nationally.", "UDISE+ 2024-25")}
    {fact(5, "65.7%", "of unemployed youth in India had secondary education or more in 2022, up from 35.2% in 2000. Only 17.5% of rural youth are in regular work.", "ILO &amp; Institute for Human Development, India Employment Report 2024")}
  </ul>
</div></section>

<section class="section band" id="theory"><div class="wrap">
  <span class="eyebrow">Theory of change</span>
  <h2>How we expect change to happen, one step at a time.</h2>
  <p class="lead">Each step builds on the one before. For every step we say what we do and what we measure, so we can tell whether it is working.</p>
  <ol class="flow">
    {toc_step(1, "start", "Starting point", "Limited awareness",
              "Students know few careers, have few role models and feel unsure in formal settings.",
              ["Baseline recorded when students join"],
              "How many careers and pathways each student can describe, and how sure they feel about deciding.")}
    {toc_step(2, "early", "Early change", "Self-knowledge and exposure",
              "Students can name their strengths and interests, and describe more careers and the routes into them.",
              ["Discover", "Build"],
              "Growth in careers described, and skills observed in practice: asking questions, explaining reasoning, contributing in a group.")}
    {toc_step(3, "decide", "Decision point", "Informed choices",
              "The stream and course after Class 10 match students’ interests, not only marks or pressure.",
              ["Discover", "Bridge"],
              "The stream and course each student chooses, and whether it matches their stated interests.")}
    {toc_step(4, "hold", "Longer term", "Pathways that hold",
              "Students stay on their chosen path, adapt to college or work, and regret their choices less.",
              ["Bridge"],
              "Where students are a year later, whether they stayed on their path, and how they feel about their choice.")}
  </ol>
  <p class="flow-foot small">Discover, Build and Bridge are the three stages of our <a href="approach.html">approach</a>.</p>
</div></section>

<section class="section" id="testing"><div class="wrap">
  <span class="eyebrow">What we are still testing</span>
  <h2>The questions we don’t have answers to yet.</h2>
  <p class="lead">Studies show that career guidance raises students’ awareness and confidence. There is almost no rigorous data from rural India on whether it changes what students actually do. Our pilot is designed to help answer these:</p>
  <div class="q-grid">
    {question(1, "Can better information outweigh family and financial pressure?", "Students often decide under pressure from home and money. We want to see whether knowing more changes the choice they make.")}
    {question(2, "Do skills built in a village school carry over to an urban college?", "Confidence in a classroom you know is not the same as confidence in a new city. We will follow students to find out.")}
    {question(3, "Do students regret their choices less?", "We could not find a reliable estimate of career-choice regret among rural Indian students. The figures that circulate come from small, mostly urban studies or commercial surveys.")}
  </div>
  <div class="promise reveal">
    <h3>What we will contribute</h3>
    <p>We are running our programme as a careful pilot. We will track whether students who go through it make choices that better match their interests, and whether they stay on those paths. We will publish the results, including results that don’t go our way.</p>
  </div>
</div></section>

<section class="section-tight band"><div class="wrap">
  <div class="report-card reveal">
    <div class="icon-tile sm"><svg class="ico" viewBox="0 0 64 64" aria-hidden="true"><path d="M16 6h22l12 12v40H16Z"/><path d="M38 6v12h12"/><path d="M24 32h18M24 40h18M24 48h10"/></svg></div>
    <div><h3>Reports</h3><p>Our first learning report will be published here after the current school year.</p></div>
  </div>
</div></section>
"""

# ---------------------------------------------------------------- Get involved
INVOLVED = """
<section class="page-hero"><div class="wrap">
  <h1>Help more rural students choose their future.</h1>
</div></section>

<section class="section"><div class="wrap">
  <h2>Ways to support our work</h2>
  <div class="ways">
    <div><h3>Fund the programme</h3><p>Our school work is currently unfunded and run by volunteers. Funding would let us hire a dedicated facilitator and reach more schools. Write to us and we will share our budget and plan.</p><a href="mailto:connects@fajarfoundation.org?subject=Funding%20Fajar%20Foundation">Ask for our budget</a></div>
    <div><h3>Partner with us</h3><p>Foundations, companies and government departments can partner with us on programme delivery, research or expansion to new districts.</p><a href="mailto:connects@fajarfoundation.org?subject=Partnership%20with%20Fajar%20Foundation">Propose a partnership</a></div>
    <div><h3>Mentor a student</h3><p>Commit an hour a month, by phone or video, to guide a student through college choices and the first years after school.</p><a href="mailto:connects@fajarfoundation.org?subject=Mentoring%20a%20Fajar%20student">Offer to mentor</a></div>
    <div><h3>Talk about your career</h3><p>Students rarely meet people outside a few familiar jobs. A 30-minute talk about your work, online or in person, can open a door.</p><a href="mailto:connects@fajarfoundation.org?subject=Career%20talk%20for%20Fajar%20students">Offer a career talk</a></div>
  </div>
</div></section>

<section class="section band"><div class="wrap">
  <h2>Before you give: our tax registration status</h2>
  <div class="note">
    <p>Fajar Foundation is a registered Section 8 company. We do <b>not yet</b> hold 12A or 80G registration, so donations to us are not currently eligible for income-tax deduction. We are also not yet registered with Form CSR-1, so companies cannot yet count funding to us as CSR spending.</p>
    <p>We will update this page as soon as our status changes. Full details are on our <a href="transparency.html">Transparency</a> page.</p>
  </div>
</div></section>
"""

# ---------------------------------------------------------------- Transparency
TRANSPARENCY = f"""
<section class="page-hero"><div class="wrap">
  <h1>Our registration, governance and finances, in one place.</h1>
</div></section>

<section class="section"><div class="wrap split split-wide">
  <div>
    <h2>Legal details</h2>
    <p>Anyone can verify our registration on the Ministry of Corporate Affairs website using our CIN.</p>
  </div>
  <div class="table-scroll">
    <table class="record">
      <tr><th scope="row">Legal name</th><td>Fajar Foundation</td></tr>
      <tr><th scope="row">Legal form</th><td>Not-for-profit company under Section 8 of the Companies Act, 2013</td></tr>
      <tr><th scope="row">Incorporated</th><td>January 2024</td></tr>
      <tr><th scope="row">CIN</th><td>{CIN}</td></tr>
      <tr><th scope="row">Registered office</th><td>At Tawlar, Pathrot, Achalpur City, Amravati - 444808, Maharashtra</td></tr>
    </table>
  </div>
</div></section>

<section class="section band"><div class="wrap split">
  <div>
    <h2>Governance</h2>
    <div class="compact-team">
      <div><b>Alim Shaikh</b><span>Co-Founder</span></div>
      <div><b>Kartik Chitrakar</b><span>Co-Founder</span></div>
      <div><b>Nitin Ingle</b><span>Internal Governance Head</span></div>
    </div>
    <p>As a Section 8 company, Fajar Foundation cannot distribute profits. Any income is used only to further our charitable objectives.</p>
  </div>
  <div>
    <h2>Documents</h2>
    <ul class="plain-list">
      <li><span class="placeholder">Certificate of Incorporation (add PDF to assets/docs/)</span></li>
      <li>Annual report 2024-25: <span class="small">to be published</span></li>
      <li>Audited financial statements: <span class="small">to be published</span></li>
    </ul>
    <p class="small">For any document not listed here, write to <a href="mailto:connects@fajarfoundation.org">connects@fajarfoundation.org</a>.</p>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <h2>How we handle student data</h2>
  <p>We collect student information only to support and track each student’s progress. We seek consent from students and their guardians, never publish identifiable details without permission, and keep records secure.</p>
</div></section>
"""

# ---------------------------------------------------------------- Contact
CONTACT = f"""
<section class="page-hero"><div class="wrap">
  <h1>Talk to us.</h1>
</div></section>

<section class="section"><div class="wrap split">
  <div>
    <p class="lead">Whether you want to fund, partner, mentor or bring Fajar to your school, the fastest way to reach us is by email or phone.</p>
    <ul class="contact-lines">
      <li><b>Email</b><a href="mailto:{EMAIL}">{EMAIL}</a></li>
      <li><b>Phone and WhatsApp</b><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></li>
      <li><b>Office</b><span>At Tawlar, Pathrot, Achalpur City,<br>Amravati - 444808, Maharashtra</span></li>
    </ul>
    <div class="actions">
      <a class="btn btn-primary" href="mailto:{EMAIL}">Write an email</a>
      <a class="btn btn-ghost" href="https://wa.me/918208186677">Message on WhatsApp</a>
    </div>
  </div>
  <div>
    <iframe class="map" title="Map of Achalpur, Amravati district" loading="lazy"
      src="https://www.openstreetmap.org/export/embed.html?bbox=77.35%2C21.18%2C77.65%2C21.35&amp;layer=mapnik"></iframe>
    <p class="small">Achalpur, Amravati district. Map © OpenStreetMap contributors.</p>
  </div>
</div></section>
"""

PAGES = [
    ("index.html", "home", "Fajar Foundation — Career readiness for rural students",
     "Fajar Foundation helps students in rural government schools in Maharashtra discover careers, build transferable skills and make informed choices, from Grade 8 onwards.", HOME),
    ("about.html", "about", "About us — Fajar Foundation",
     "Why Fajar Foundation exists, what we stand for, and the people behind it.", ABOUT),
    ("approach.html", "approach", "Our approach — Fajar Foundation",
     "Discover, Build, Bridge: how Fajar Foundation prepares rural students for their careers.", APPROACH),
    ("where-we-work.html", "where", "Where we work — Fajar Foundation",
     "Fajar Foundation works in government tribal residential schools in Melghat, Amravati district, Maharashtra.", WHERE),
    ("evidence.html", "evidence", "Evidence — Fajar Foundation",
     "The data behind the problem, the gap in the evidence, and Fajar Foundation’s theory of change.", EVIDENCE),
    ("get-involved.html", "involved", "Support our work — Fajar Foundation",
     "Fund, partner, mentor or give a career talk to support rural students.", INVOLVED),
    ("transparency.html", "transparency", "Transparency — Fajar Foundation",
     "Registration, governance and documents of Fajar Foundation, a Section 8 company.", TRANSPARENCY),
    ("contact.html", "contact", "Contact — Fajar Foundation",
     "Email, phone and office address for Fajar Foundation, Achalpur, Amravati.", CONTACT),
]

if __name__ == "__main__":
    for args in PAGES:
        page(*args)
    page("404.html", "none", "Page not found — Fajar Foundation", "Page not found.",
         '<section class="page-hero"><div class="wrap"><h1>This page doesn’t exist.</h1><p class="lead">It may have moved. Go back to the <a href="index.html">home page</a> or <a href="contact.html">contact us</a>.</p></div></section>')
    print("built", len(PAGES), "pages")
