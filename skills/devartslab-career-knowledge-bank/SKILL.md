---
name: career-knowledge-bank
description: Convert historical career information from multiple sources into a single interconnected career knowledge bank that preserves facts, stories, voice, terminology, and evidence for future role-specific extraction and reinterpretation
---

<!-- author: Amir Olyaei | DevArts Lab (devartslab.com) | last updated: 2026-09-04 -->

# Historical Career Content Bank

## Purpose

Convert bulk historical career information from multiple sources into a single interconnected career content bank.

Supported inputs include:

academic transcripts
educational records
course lists
degrees
certificates
training records
previous resumes
role-tailored resumes
job applications
portfolio content
project documentation
employment records
apprenticeship records
professional development
certifications
awards
other career-related historical information

The output is NOT a resume.

The output is NOT a collection of separate resume sections.

The output is a reusable historical content bank from which role-specific content can later be extracted.

## Core Output Model

Every input source becomes one compact wrapped content block.

Multiple source blocks are separated by:

||

Do not use repeated headings, numbering, explanations, bullets, or verbose labels between source blocks unless necessary for preserving source identity.

Preferred structure:

[wrapped source 1] || [wrapped source 2] || [wrapped source 3]

All source blocks collectively form one interconnected historical content bank.

## Wrapping Rule

Within each source block:

preserve historical facts
preserve useful terminology
preserve course titles
preserve skills
preserve concepts
preserve tools
preserve technologies
preserve dates
preserve grades
preserve GPAs
preserve credentials
preserve accomplishments
preserve relevant phrases
preserve transferable concepts

Connect related information using compact separators.

Preferred internal separator:

/

Example:

Boston Architectural College / Boston, Massachusetts / Graduate studies / M.Architecture / Architecture / 2012 Fall / 2013 Spring / Design Principles / Architectural Design / Design Studio / Spatial Design / AutoCAD I-2D / AutoCAD II-3D / AutoCAD / 2D CAD / 3D CAD / Computer-Aided Design / Technical Drawing / 2D Drafting / 3D Drafting / Visual Communication / Design Thinking / Spatial Thinking / Creative Problem Solving / Visual Representation

## Bulk Input Handling

When multiple historical sources are provided together, process each source independently first.

For each source:

extract
normalize
consolidate
remove unnecessary duplication
identify related terminology
identify transferable concepts
preserve factual evidence
wrap the resulting information into one compact block

Then connect the blocks using:

||

Do not merge unrelated source facts into a single indistinguishable sequence if doing so would destroy source context.

Do not create verbose source labels merely to separate inputs.

## Example Bulk Output

Input sources may include:

Transcript
Previous Frontend Developer resume
Previous UI/UX resume
Project history

Output:

Boston Architectural College / Boston, Massachusetts / M.Architecture / Architecture / Design Principles / Architectural Design / Design Studio / Spatial Design / AutoCAD I-2D / AutoCAD II-3D / 2D CAD / 3D CAD / Computer-Aided Design / Technical Drawing / Visual Communication / Design Thinking / Spatial Thinking / Creative Problem Solving / 3.33 Cumulative GPA || React / Next.js / JavaScript / TypeScript / frontend development / component development / responsive interfaces / UI development / reusable components / web development || User Interface Design / User Experience / visual hierarchy / responsive design / accessibility / design systems / prototyping / user-centered design || project development / Git / GitHub / API integration / database integration / deployment / collaboration

The entire result is one historical content bank.

The `||` delimiter identifies the boundary between original bulk inputs without requiring verbose headings.

## Historical Preservation

Never discard information simply because it does not appear relevant to the user's current target role.

Historical information may become relevant to another role later.

Maintain one source of truth.

Do not create a separate permanent content bank for every job title.

## Deduplication

Remove exact duplicates.

Remove obvious repetitions when the repeated occurrence adds no additional meaning.

Preserve distinct variants when they have retrieval value.

Example:

AutoCAD
AutoCAD I-2D
AutoCAD II-3D
2D CAD
3D CAD
Computer-Aided Design

remain together because they provide different useful retrieval terms.

Do not collapse everything into:

AutoCAD

Likewise preserve:

React
React.js
component development
reusable components
frontend development
UI development

when each term provides useful retrieval value.

## Semantic Connections

Connect terminology that represents related knowledge.

Example:

Architectural Design / Design Studio / Spatial Design / Visual Design / Design Principles / Design Thinking / Spatial Thinking / Visual Communication / Visual Representation / Creative Problem Solving

Technical design:

AutoCAD / 2D CAD / 3D CAD / Computer-Aided Design / Technical Drawing / 2D Drafting / 3D Drafting / Technical Design

Academic evidence:

A AutoCAD I-2D / A 3D Design / A- 2D Design Draw / A- AutoCAD II-3D / C+ Freehand Drawing / 3.33 Cumulative GPA / 3.08 Fall 2012 GPA / 3.85 Spring 2013 GPA

## Resume Sources

When processing an existing resume:

preserve job titles
preserve employers
preserve dates
preserve responsibilities
preserve accomplishments
preserve technologies
preserve tools
preserve projects
preserve skills
preserve terminology
preserve role-specific keywords
preserve transferable concepts

A resume tailored for one role is still historical source material.

Do not restrict its terminology to that role.

If multiple tailored resumes use different terminology, preserve useful terminology from each while removing unnecessary duplication.

## Academic Sources

For transcripts and educational records:

preserve institution
location
degree
program
major
concentration
courses
terms
credits
grades
GPAs
academic performance
course-specific evidence

Extract transferable concepts from coursework when reasonably supported.

Do not convert coursework into professional employment experience.

Do not imply professional mastery solely from a course.

## Professional Sources

For employment, apprenticeship, volunteer, project, or professional-development sources:

preserve organization
role
dates
responsibilities
technologies
tools
projects
achievements
methods
domains
collaboration
technical capabilities
business capabilities
professional terminology

Maintain distinctions between:

employment
education
training
projects
volunteer work
certifications
independent work

## Terminology Expansion

Extract useful terminology supported by the source.

Include:

original wording
common equivalent terminology
abbreviations
expanded terminology
related technical terminology
related conceptual terminology
transferable terminology
domain terminology

Do not invent unsupported expertise.

Example:

AutoCAD II-3D / AutoCAD / 3D CAD / Computer-Aided Design / 3D Drafting / Technical Design / 3D Visualization

## Evidence Integrity

Every factual claim must be supported by the input.

Do not transform:

coursework into employment
training into professional experience
interest into expertise
exposure into mastery
a project into employment
a keyword into demonstrated proficiency

Preserve the distinction between:

professional experience
academic experience
training
project experience
transferable capability
conceptual knowledge

## Provenance

Every meaningful piece of information should be traceable internally to its source.

For example:

React / reusable components / component architecture / UI consistency

could internally relate back to:

Resume 2025 / Bullet 3

while:

M.Architecture / Design Studio / AutoCAD II-3D

relates back to:

BAC Transcript

Provenance does not need to appear in the compact content bank output.

The compiler should preserve it internally.

This becomes valuable when later asking:

Where did this skill come from?

Is this terminology actually supported by my history?

## Evidence vs Capability

Distinguish these stages:

SOURCE -> EVIDENCE -> CAPABILITY -> INTERPRETATION -> TARGET EXPRESSION

SOURCE
The raw input material.

EVIDENCE
What the source demonstrates happened.

CAPABILITY
A transferable ability reasonably derived from evidence.

INTERPRETATION
A professional reading of that capability.

TARGET EXPRESSION
How to communicate it for a specific role.

Example:

Design Studio (source) -> course project evidence (evidence) -> spatial design (capability) -> design thinking (interpretation) -> product design (target expression)

This progression should remain traceable to protect against accidental inflation.

Do not skip directly from source to target expression without the intermediate stages.

## Conflicting Sources

If two historical sources conflict:

do not silently invent a resolution
prefer the clearly authoritative or explicitly updated source
preserve meaningful historical distinctions when necessary
do not fabricate missing information

## Dates

Preserve dates when they establish historical context.

Keep dates connected to:

degrees
courses
employment
projects
training
certifications
career progression
academic performance

## Output Style

Use compact keyword-oriented content.

Do not turn the content into polished prose.

Do not add grammatical filler.

Do not explain the extraction process.

Do not add commentary between source blocks.

Do not create unnecessary headings.

Do not use bullets unless the user specifically requests them.

Use:

/

to connect related information within a source block.

Use:

||

to separate bulk input source blocks.

## Token Efficiency

Optimize the output for compactness.

Prefer:

React / TypeScript / JavaScript / frontend development / component development

over:

React, TypeScript, and JavaScript, with experience in frontend and component development.

Prefer:

Boston Architectural College / M.Architecture / Architecture / 2012 Fall / 2013 Spring

over:

Boston Architectural College, where the user studied Architecture in the M.Architecture program during Fall 2012 and Spring 2013.

Do not repeat:

source names
category names
explanations
contextual phrases
grammatical connectors

unless needed for accuracy.

## Future Retrieval

The content bank must support future requests such as:

extract content for Frontend Developer
extract content for Software Developer
extract content for UI/UX Designer
extract content for Architectural Designer
extract content for Cloud Developer
extract content for AI Software Engineer
tailor my resume for this job
find all relevant historical skills
identify transferable experience
extract relevant education
extract relevant technical terminology

When a target role is provided later:

search the entire interconnected content bank
identify directly relevant information
identify adjacent information
identify transferable concepts
identify relevant terminology
identify supporting evidence
prioritize role relevance
preserve evidence integrity

Do not modify the historical source of truth merely because a particular role requires different terminology.

## Final Validation

Before output:

preserve all meaningful historical facts
preserve useful terminology
preserve source distinctions
preserve dates
preserve academic evidence
preserve professional evidence
remove unnecessary duplicates
retain meaningful variants
connect related information
avoid unsupported claims
avoid artificial resume language
use `/` for compact internal connections
use `||` between bulk source inputs
keep the entire result as one reusable historical content bank

## Default Behavior

Whenever the user provides historical career information:

extract everything useful
connect related information
remove unnecessary duplication
wrap each bulk source independently
separate source blocks with `||`
preserve the entire historical record
return the compact interconnected content bank

The result should be treated as a long-term historical career source of truth, not as a finished resume.

# Terminology Evolution and Seniority Adaptation

## Purpose

Maintain historical information as the source of truth while allowing its terminology, interpretation, communication level, and presentation to evolve with the user's career.

Historical information must remain stable.

Professional terminology may evolve.

Communication complexity may evolve.

Target-audience framing may evolve.

Seniority positioning may evolve.

Never alter historical facts merely to make the user appear more senior.

## Career Model Layers

Maintain these conceptual layers:

HISTORICAL SOURCE OF TRUTH
CAREER INTERPRETATION
TERMINOLOGY / SENIORITY LAYER
TARGET COMMUNICATION

Additionally, two attributes are associated with historical material and generated communication:

STORY BANK
VOICE

Story and Voice are not layers that modify facts.
They are attributes associated with historical material and generated communication.

### Historical Source of Truth

Contains what actually happened.

Preserve:

roles
responsibilities
projects
technologies
tools
courses
education
training
certifications
achievements
dates
metrics
terminology
source wording
historical evidence

Do not rewrite this layer based on target job requirements.

### Career Interpretation

Translate historical evidence into professional concepts.

Identify:

technical capabilities
professional capabilities
transferable capabilities
domain knowledge
architectural concepts
design concepts
engineering concepts
business concepts
problem-solving concepts
leadership concepts
systems concepts

Interpretation may evolve as the user's career develops.

### Target Communication

Adapt the interpreted information for:

target job title
target seniority
industry
company
job description
audience
communication medium
technical depth
professional context

The target communication layer may use terminology that is more sophisticated than the original historical wording when that terminology accurately represents the user's demonstrated capabilities.

## Seniority Adaptation

Terminology must reflect the user's actual career level.

Do not automatically use senior terminology merely because it sounds stronger.

Increase terminology sophistication only when supported by accumulated experience.

Possible progression:

ENTRY / EARLY CAREER
implementation
development
building
learning
using
supporting
contributing
collaborating

MID CAREER
designing
developing
integrating
optimizing
architecting
owning
delivering
leading implementation

SENIOR
architecture
technical strategy
system design
scalability
technical direction
cross-functional leadership
mentorship
technical ownership
decision-making
standards
platform thinking

STAFF / PRINCIPAL
technical strategy
architecture direction
organizational impact
system-wide design
technical vision
platform strategy
cross-team alignment
engineering standards
technical governance
long-term scalability

Only use terminology from a higher level when historical evidence supports the underlying responsibility or capability.

## Terminology Evolution

Historical terminology may have multiple professional representations.

Maintain:

original terminology
equivalent terminology
modern terminology
industry terminology
seniority-appropriate terminology
target-role terminology

Example:

Historical:

AutoCAD / 3D CAD / Technical Drawing / 3D Drafting

Possible interpretations:

Computer-Aided Design / technical design / 3D visualization / digital design

Possible target terminology:

digital design workflows / technical visualization / spatial modeling

Do not replace the historical terminology.

Add professionally useful interpretations alongside it.

## Terminology Mapping

When appropriate, internally maintain mappings such as:

historical term -> professional concept -> modern terminology -> target-role terminology

Example:

Design Studio
-> design process
-> iterative design
-> product / UX design process

Visual Communication
-> communication of information through visual systems
-> visual information design
-> user interface communication

Technical Drawing
-> technical representation
-> digital technical documentation
-> technical visualization

AutoCAD
-> Computer-Aided Design
-> digital drafting
-> CAD workflow

Do not output the mapping unless requested.

Use it for future extraction and adaptation.

## Career Growth

Treat the career content bank as cumulative.

Year 1:

historical knowledge + foundational terminology

Year 2:

historical knowledge + expanded terminology + demonstrated application

Year 3:

historical knowledge + advanced terminology + broader ownership

Later career:

historical knowledge + specialized terminology + systems thinking + strategic framing

Do not overwrite previous terminology.

Accumulate new terminology as the user's demonstrated responsibilities grow.

## Seniority Evidence

Higher-level terminology should be supported by evidence such as:

increased responsibility
technical ownership
architecture decisions
system design
cross-functional collaboration
mentorship
leadership
project ownership
stakeholder communication
technical strategy
scalability decisions
process improvement
standards development
organizational impact
business impact

Do not infer seniority solely from years elapsed.

## Contextual Seniority

Seniority is not a single value. Distinguish three types:

JOB TITLE SENIORITY
What the person was officially called.

CAPABILITY SENIORITY
The level of responsibility demonstrated.

COMMUNICATION SENIORITY
The sophistication with which the capability can be described.

These three do not always match.

Someone can be a senior frontend engineer while having relatively limited leadership experience.
Someone else can have staff-level architectural responsibility without formally holding a Staff title.

Use this distinction to produce accurate target communication rather than assuming a single seniority level across all dimensions.

## Target Audience Adaptation

Adapt terminology according to audience.

### Technical Audience

Prefer:

architecture
implementation
APIs
systems
components
data flows
infrastructure
performance
scalability
testing
deployment
technical tradeoffs

### Hiring Manager

Balance:

technical capabilities
ownership
delivery
problem solving
collaboration
impact
business relevance

### Recruiter

Prioritize:

recognized job-title terminology
core technologies
relevant skills
domain keywords
seniority indicators
measurable accomplishments

### Executive Audience

Prioritize:

outcomes
business impact
strategy
scale
risk
efficiency
organizational value

Do not overload executive communication with implementation details.

## Target Role Adaptation

The same historical evidence may map differently to different roles.

Do not create new historical facts for the target role.

Instead, select the relevant interpretation.

Example:

Historical:

Design Principles / Visual Communication / Spatial Thinking / Creative Problem Solving

Frontend Developer:

UI development / visual communication / interface design / user-centered thinking

UI/UX Designer:

visual communication / spatial thinking / design principles / user-centered design

Architectural Designer:

spatial design / architectural design / technical design / visual representation

Product Designer:

design thinking / visual communication / problem solving / user-centered design

The historical source remains identical.

The terminology selected for communication changes.

## Terminology Confidence

Classify terminology internally by evidence strength.

DIRECT

Explicitly stated in the historical source.

SUPPORTED

A reasonable professional interpretation of explicit historical information.

TRANSFERABLE

A capability reasonably transferable to another domain.

ADJACENT

Related terminology that may be useful but requires contextual validation.

INFERRED

A possible interpretation that should not be presented as established expertise without additional evidence.

Prefer DIRECT and SUPPORTED terminology.

Use TRANSFERABLE terminology carefully.

Do not present INFERRED terminology as fact.

## No False Seniority

Never use:

led
architected
owned
managed
strategized
directed
mentored
designed systems
defined architecture
established standards

unless the historical evidence supports the underlying responsibility.

A sophisticated term is acceptable only when the associated capability is truthful.

## Communication Maturity

As seniority increases, communication should progressively emphasize:

early career:

what was built

mid career:

how it was built and why

senior:

why decisions were made, what was owned, and what impact resulted

staff / principal:

technical direction, systems impact, organizational alignment, and strategic outcomes

Do not artificially inflate communication complexity.

The goal is greater precision, not unnecessary complexity.

## Historical Preservation Rule

Never modify the historical content bank when adapting terminology.

Instead:

SOURCE OF TRUTH

- CAREER INTERPRETATION
- TARGET TERMINOLOGY
- TARGET AUDIENCE
- TARGET SENIORITY

produce the final communication.

Historical facts are immutable.
Historical interpretations are revisable.
Historical narratives are reusable but never binding.

The historical content bank remains stable unless the user explicitly corrects or updates historical information.

## Annual Career Evolution

When new career information is provided:

do not replace older information
do not downgrade previous terminology
do not delete earlier terminology
do not duplicate unchanged information

Instead:

add new evidence
add newly demonstrated capabilities
add more advanced terminology when supported
update career interpretation
expand seniority vocabulary
retain historical terminology
strengthen target-role mappings

The content bank therefore becomes progressively richer as the user's career develops.

## Final Principle: Terminology and Seniority

Historical data answers:

"What actually happened?"

Career interpretation answers:

"What professional capability does that history demonstrate?"

Seniority adaptation answers:

"How sophisticated can that capability accurately be described today?"

Target adaptation answers:

"Which terminology best communicates that capability to this role and audience?"

Never confuse these four questions.

# Narrative and Voice Preservation

## Purpose

Preserve what existed.

Preserve the user's original storytelling, tone, phrasing, emphasis, and narrative structure when processing resumes and other personally written career documents.

This section is responsible for preservation, not for constraining future use.

A resume is not only a collection of facts.

Individual bullets may contain:

personal storytelling
problem framing
cause-and-effect relationships
technical narrative
decision-making narrative
impact narrative
personal emphasis
distinctive phrasing
communication style
tone
voice
context
sequence of events

These elements must not be lost during extraction.

## Bullet-Level Preservation

Treat every resume bullet as an independent historical narrative unit.

For each meaningful bullet, preserve:

ORIGINAL BULLET
FACTUAL EVIDENCE
STORY / NARRATIVE
CAPABILITIES
TERMINOLOGY
IMPACT
VOICE / TONE

Do not reduce a complete bullet to keywords alone.

## Original Bullet Preservation

When the source is a resume or personally written professional document, preserve the complete original bullet whenever practical.

The original wording is historical source material.

Do not silently rewrite it during compilation.

Example:

ORIGINAL: Built a reusable component system that helped the team move faster when developing new pages, while keeping the interface consistent across the application.

The original sentence must remain recoverable even if its terminology is later extracted and normalized.

## Story Preservation

Identify the underlying story within each bullet.

Preserve relationships such as:

problem -> action -> result

challenge -> approach -> outcome

need -> solution -> impact

technical decision -> implementation -> consequence

responsibility -> execution -> achievement

Before -> intervention -> after

Do not flatten these relationships into disconnected keywords.

Example:

Original:

Built a reusable component system that helped the team move faster when developing new pages, while keeping the interface consistent across the application.

Story:

reusable components -> faster page development -> interface consistency

Preserve this relationship for future resume generation.

## Voice Preservation

Identify distinctive characteristics of the user's writing.

Preserve:

directness
technical specificity
level of detail
sentence rhythm
word choice
degree of formality
personal emphasis
cause-and-effect framing
problem-solving style
impact framing
descriptive style

Do not automatically replace the user's natural voice with generic resume language.

Avoid converting every bullet into standardized corporate language.

## Tone Profile

When sufficient writing samples exist, infer a reusable tone profile from the user's actual writing.

Possible dimensions:

direct <-> narrative
technical <-> accessible
concise <-> descriptive
formal <-> conversational
implementation-focused <-> outcome-focused
humble <-> assertive
individual-focused <-> team-focused
technical-detail-heavy <-> high-level

The tone profile is an interpretation of the user's writing, not a fact about the user.

Use it to preserve stylistic consistency in future generated content.

## Story Bank

In addition to the historical content bank, maintain a conceptual story bank.

The story bank is defined as:

historical narratives + narrative elements + relationships + possible framings

It contains reusable narratives extracted from:

resume bullets
project descriptions
cover letters
portfolio descriptions
professional statements
interview stories
other personally written career content

Each story should retain:

original narrative
context
problem
action
technical approach
reasoning
result
impact
distinctive framing
original wording
narrative elements
relationships between elements
possible framings

A story is not necessarily about how the user experienced something.
It captures narrative possibilities derived from evidence.

The same experience may become a technical story, architecture story, leadership story, product story, or business story depending on the target.

Do not reduce the story bank to keywords.

## Relationship Between Content Bank and Story Bank

The Historical Content Bank answers:

WHAT information exists?

The Story Bank answers:

WHAT narratives, narrative elements, relationships, and possible framings can be derived from this evidence?

The Terminology Layer answers:

HOW can the same evidence be described at the user's current professional level?

The Target Communication Layer answers:

HOW should it be communicated to this particular role and audience?

These layers must remain distinct.

## Terminology Adaptation Without Story Loss

When adapting a historical bullet for a higher-seniority role:

preserve the original story
preserve the factual sequence
preserve the actual contribution
preserve the actual outcome

Then improve terminology only where supported.

Example progression:

Original:

Built reusable components to make page development faster and keep the UI consistent.

Intermediate:

Developed reusable component patterns that improved page development efficiency and UI consistency.

Advanced:

Developed reusable frontend component patterns that improved development velocity and established greater consistency across application interfaces.

The terminology evolves.

The underlying story does not.

## Voice Adaptation

When generating future content:

Start from the preserved original story and voice.

Then apply:

target role
target seniority
target audience
industry terminology
job-description terminology

Do not start from generic job-description language and attempt to reconstruct the user's voice afterward.

## Personal Story Priority

When multiple valid ways exist to describe the same experience, prefer the user's original narrative framing over generic industry phrasing.

Example:

If the user consistently explains work through:

problem -> solution -> practical impact

preserve that structure.

If the user emphasizes:

technical challenge -> experimentation -> implementation

preserve that structure.

If the user emphasizes:

team need -> contribution -> outcome

preserve that structure.

The user's recurring narrative patterns are part of their professional communication identity.

## No Voice Erasure

Do not:

replace distinctive wording with generic buzzwords
remove contextual details that make a story unique
convert every bullet into keyword lists
replace personal framing with corporate phrasing
standardize all bullets into identical sentence structures
remove cause-and-effect relationships
remove technical reasoning
remove meaningful narrative details merely for brevity

Compression is allowed only when the user requests it.

## Source Priority

When generating from a historical resume:

1. Preserve factual evidence.
2. Preserve the original story.
3. Preserve distinctive voice.
4. Preserve meaningful terminology.
5. Adapt terminology to seniority.
6. Adapt terminology to target role.
7. Adapt communication to target audience.
8. Optimize length and keyword relevance.

Never reverse this order.

## Future Resume Generation

When generating a new resume bullet:

retrieve the most relevant historical story first.

Then retrieve supporting evidence.

Then retrieve current seniority terminology.

Then retrieve target-role terminology.

Then formulate the bullet.

The generated bullet should feel like an evolution of the user's original professional story, not a completely different person writing about it.

## Original-to-Adapted Traceability

Whenever practical, maintain an internal relationship:

ORIGINAL BULLET
-> HISTORICAL EVIDENCE
-> STORY
-> CURRENT TERMINOLOGY
-> TARGET TERMINOLOGY
-> GENERATED BULLET

This allows future content to evolve while remaining grounded in the original source.

## Multiple Resume Versions

If the same experience appears across multiple resumes:

preserve the original versions.

Do not discard a version simply because another version is newer.

Compare them for:

new terminology
different storytelling
different emphasis
different impact framing
different audience adaptation
different seniority level

Treat the evolution itself as useful historical information.

## Career Voice Evolution

The user's writing style may also mature over time.

Do not force all historical writing into the latest voice.

Preserve:

earlier voice
later voice
current voice

When generating current professional content, use the current voice while retaining older stories and evidence.

Career growth should change how the user communicates their experience without erasing how those experiences were originally described.

## Final Principle: Narrative and Voice

Do not compile the user's resume into keywords only.

Compile:

FACTS + STORIES + VOICE + TERMINOLOGY + EVIDENCE

The historical content bank preserves what happened.

The story bank preserves how the user tells what happened.

The terminology layer allows professional language to evolve.

The target communication layer adapts the result to the role and audience.

Nothing should be lost merely because the user's career language becomes more sophisticated.

# Narrative Flexibility and Perspective Evolution

## Purpose

Prevent what existed from becoming a constraint.

## Core Principle

Preserve historical stories without treating them as permanent narrative templates.

Preserve the original story as an artifact, not as the only story.

An original story is historical evidence of how the user communicated an experience at a particular point in time.

It must remain recoverable.

It must NOT constrain future storytelling.

Future storytelling may:

reinterpret the experience
change the emphasis
change the narrative structure
change the audience
change the professional perspective
change the terminology
change the perceived significance
highlight different outcomes
connect the experience to new capabilities
connect the experience to a new industry
connect the experience to a new career direction

The compiler must preserve history while maximizing future narrative flexibility.

## Historical Story vs Current Story

Maintain a strict distinction between:

ORIGINAL STORY
CURRENT INTERPRETATION
POTENTIAL INTERPRETATIONS
TARGET STORY

ORIGINAL STORY:

How the user described the experience in the source document.

CURRENT INTERPRETATION:

How the experience can reasonably be understood based on the user's accumulated career history.

POTENTIAL INTERPRETATIONS:

Other legitimate perspectives supported by the same evidence.

TARGET STORY:

The narrative selected and written for the current opportunity.

None of these should overwrite the others.

## No Narrative Lock-In

Never treat:

original wording
original bullet structure
original emphasis
original terminology
original framing
original career objective

as permanent constraints.

The original narrative is preserved for provenance, not mandatory reuse.

A future version may use a completely different narrative structure when appropriate.

## Narrative Reframing

The same historical experience may support multiple legitimate stories.

Possible dimensions of reframing include:

technical implementation
problem solving
design
user impact
business impact
efficiency
quality
scalability
innovation
collaboration
ownership
leadership
learning
adaptability
systems thinking
process improvement
strategic thinking
cross-functional contribution

Select the framing according to the current goal.

Do not assume the framing used in the original resume was the only meaningful interpretation.

## Career Perspective Evolution

As the user's career develops, allow the meaning and significance of historical experiences to be reconsidered.

An experience originally presented as:

"implemented a feature"

may later be understood as:

"contributed to application architecture"

if subsequent evidence establishes broader architectural responsibility.

An experience originally presented as:

"created a UI"

may later be relevant to:

design systems
component architecture
user experience
product thinking
frontend architecture

when supported by accumulated evidence.

The historical event does not change.

The professional interpretation may evolve.

## New Industries

Do not preserve stories only within the terminology or conceptual boundaries of the industry in which they originally occurred.

When entering a new industry:

identify transferable underlying capabilities
identify alternative professional interpretations
identify industry-specific terminology
identify new stakeholder perspectives
identify new outcomes that are genuinely supported
reframe the story accordingly

Do not invent industry experience.

Translate transferable experience instead.

## New Career Goals

A historical story may become relevant to a future goal that did not exist when the story was originally written.

Do not discard historical stories because they were written for a previous career direction.

Instead:

retrieve the underlying evidence
separate evidence from previous framing
identify transferable capabilities
identify alternative interpretations
reconstruct the narrative around the new goal

## New Opportunities

For every new opportunity, treat the historical story as raw narrative material rather than a fixed template.

Ask internally:

What happened?

What did the user actually do?

What problem existed?

What decisions were made?

What changed?

What evidence demonstrates the contribution?

What other legitimate perspectives does this experience support?

Which perspective is strongest for this opportunity?

Which terminology fits the target role?

Which terminology fits the user's current seniority?

Which framing fits the audience?

Then construct a new narrative.

## Narrative Choice

Do not always choose the original story.

Choose the strongest truthful story for the current objective.

Possible selection criteria:

target role relevance
target industry relevance
seniority
audience
business relevance
technical relevance
leadership relevance
user impact
measurable impact
strategic relevance
career direction
job-description terminology

The original story remains available as a reference but does not control the final narrative.

## Story Decomposition

When processing a resume bullet, separate:

EVENT
ACTION
CONTEXT
PROBLEM
DECISION
METHOD
TECHNOLOGY
RESULT
IMPACT
LESSON
PERSPECTIVE
VOICE
ORIGINAL WORDING

This decomposition increases future flexibility.

A future narrative can recombine these elements differently.

## Narrative Recombinations

Allow future bullets to emphasize different components.

Technical:

problem -> technical decision -> implementation -> technical result

Product:

user need -> solution -> user outcome

Business:

business problem -> intervention -> efficiency / value

Leadership:

challenge -> ownership -> alignment -> outcome

Architecture:

constraint -> architectural decision -> system consequence

Collaboration:

cross-functional problem -> contribution -> alignment -> outcome

Learning:

challenge -> experimentation -> capability gained -> application

All narratives must remain grounded in the same historical evidence.

## Voice Independence

Preserve the user's original voice without forcing future writing to imitate it exactly.

Voice preservation means:

retain the ability to recover the user's natural communication patterns

not:

freeze every future document into the same writing style

The user's voice may mature, become more technical, become more strategic, become more concise, or adapt to different professional environments.

Allow that evolution.

## Perspective Independence

Do not assume that the user's current interpretation is their final interpretation.

Historical evidence may support future perspectives that have not yet been identified.

Therefore:

preserve evidence broadly
preserve multiple interpretations
avoid premature classification
avoid permanent narrative labels
avoid assigning one definitive meaning to an experience

## Opportunity-Specific Storytelling

Every target opportunity may produce a different valid story from the same historical evidence.

The system may generate:

Resume version
LinkedIn version
Portfolio version
Cover-letter version
Interview version
Technical interview version
Executive-facing version
Industry-transition version
Leadership version
Startup version
Enterprise version

These are not contradictory simply because they emphasize different aspects of the same experience.

## Narrative Supersession

New storytelling does not delete old storytelling.

Instead:

old story = historical narrative

new story = current narrative

different target story = contextual narrative

All may coexist.

A later story may be more sophisticated without making the earlier story incorrect.

## Final Principle: Narrative Flexibility

Preserve the user's stories.

Do not preserve them as constraints.

Preserve the evidence beneath the stories.

Preserve the original narratives as historical artifacts.

Preserve the user's ability to reinterpret those experiences.

Allow new perspectives.

Allow new terminology.

Allow new industries.

Allow new career goals.

Allow new audiences.

Allow new seniority levels.

Allow entirely different narrative structures.

The system should maximize future storytelling possibilities while maintaining historical truth.

The objective is:

PRESERVE HISTORY

- PRESERVE VOICE
- PRESERVE EVIDENCE
- PRESERVE NARRATIVE OPTIONS
- ENABLE REINTERPRETATION
- # ENABLE CAREER EVOLUTION
  FLEXIBLE LONG-TERM CAREER SOURCE OF TRUTH

## Governing Principle

The system must preserve the past without allowing the past to define the future.

## Overall Architecture

HISTORICAL SOURCES
|
EVIDENCE BANK
|
CONTENT / KNOWLEDGE BANK
|
CAPABILITY INTERPRETATION
|
TERMINOLOGY + SENIORITY EVOLUTION
|
STORY BANK + NARRATIVE OPTIONS
|
TARGET ROLE + INDUSTRY + AUDIENCE
|
CURRENT COMMUNICATION

Nothing downstream rewrites the historical source.

The system is a long-term career knowledge and narrative system that can continuously reinterpret the same evidence as the user's career develops, without falsifying or losing the history.
