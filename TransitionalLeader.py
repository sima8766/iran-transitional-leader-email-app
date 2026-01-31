# app.py
# Email Draft Generator (Bulk BCC) - Link-based references (YouTube + Imgur album)
# - Links are clickable in email clients
# - Picks a new random template each time (different from last pick)

import random
import urllib.parse
from pathlib import Path

import pandas as pd
import streamlit as st


# ---------------------------
# Paths
# ---------------------------
BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "au_parliament_contacts.csv"


# ---------------------------
# Page config
# ---------------------------
st.set_page_config(page_title="Email Draft Generator", layout="centered")
#st.title("Email Draft Generator for Australian Senators and MPs in Support of the Iranian National Revolution")
#st.title("Email Draft Generator for Australian Parliamentarians | تولید پیش‌نویس ایمیل برای نمایندگان پارلمان استرالیا")
#st.header("Email Draft Generator for Australian Parliamentarians in Support of the Iranian National Revolution and Crown Prince Reza Pahlavi as a Transitional Leader | تولید پیش‌نویس ایمیل برای نمایندگان پارلمان استرالیا در حمایت از انقلاب ملی ایران و شاهزاده رضا پهلوی به‌عنوان رهبر دوران گذار")
st.markdown(
    "<h3 style='text-align:center;'>Sending Email to Australian Parliamentarians in Support of the Iranian National Revolution and Crown Prince Reza Pahlavi as a Transitional Leader</h3>",
    unsafe_allow_html=True
)

st.markdown(
    "<h5 style='text-align:center; direction:rtl;'>ارسال ایمیل به نمایندگان پارلمان استرالیا در حمایت از انقلاب ملی ایران و شاهزاده رضا پهلوی به‌عنوان رهبر دوران گذار</h5>",
    unsafe_allow_html=True
)

st.caption("Enter your name and open a prefilled email with all recipients included in BCC.")
#st.info("This tool can be used by anyone, anywhere in the world, no matter where you live.")
st.info("This tool can be used by anyone, anywhere in the world, no matter where you live. | این ابزار برای همه افراد، در هر نقطه‌ای از جهان و فارغ از محل سکونت، قابل استفاده است.")


# ---------------------------
# References (updated: attributed to Reza Pahlavi + Imgur photos link)
# ---------------------------
REFERENCES_BLOCK = (
    "Additional references:\n"
    "• Reza Pahlavi’s remarks on how a free Iran would benefit global stability:\n"
    "https://youtu.be/pzlKh8B2GFE?si=WXWMw2IaxMNC16kp\n\n"
    "• Reza Pahlavi’s interview with ARD (Germany’s nightly news, English from 0:18):\n"
    "https://youtu.be/sfd2hNuK498?si=4dPK_i1gngkr-hLT\n\n"
    "• Reza Pahlavi’s full international press conference addressing transition and governance:\n"
    "https://www.youtube.com/live/GIYZhaoiFYU?si=orGTYn8FFMSB-HBh\n\n"
    "• Photographic documentation from inside Iran showing public expressions of support for Reza Pahlavi:\n"
    "https://imgur.com/a/s9gKZbx"
)

# This exact bilingual requirement must appear in ALL templates:
SLOGANS_REQUIRED = '“Javid Shah” (“Long live the King”) and “Pahlavi bar migardeh” (“Pahlavi will return”)'


# ---------------------------
# 20 BODY-ONLY templates (greeting + signature are added separately)
# Each template includes the required slogans with translations in parentheses.
# ---------------------------
EMAIL_TEMPLATES = [
    f"""I am writing regarding the ongoing situation in Iran and how the international community can best stand with and support the brave people who are fighting bare-handed for their freedom against the brutal regime, and help advance a peaceful and democratic transition.

Despite severe repression, internet shutdowns, as well as risks to their very lives, voices from inside Iran have become increasingly clear and consistent. Across many cities, people are publicly calling for Reza Pahlavi to guide a transitional process and lead their revolution, holding placards with his name and photo and chanting {SLOGANS_REQUIRED}. These calls are emerging from within Iran itself and reflect a growing demand for national unity and a credible alternative to the current regime.

Reza Pahlavi has publicly outlined a clear and structured roadmap for transition, grounded in democratic principles, human rights, free elections, and the separation of religion and state. He has emphasised that his role would be to facilitate a transitional period and return decision-making power to the Iranian people through a democratic referendum.

Given the scale of violence, massacres, and the regime’s crimes against its own people inside Iran and the systematic silencing of independent media, along with widespread propaganda aimed at distorting facts and suppressing dissenting voices, international recognition of the expressed will of the Iranian people is critically important. Constructive engagement with a credible transitional framework can help deter further repression and support stability, both regionally and globally.

Thank you for your time and consideration.

{REFERENCES_BLOCK}""",

    f"""I write to draw attention to the ongoing crisis in Iran and to highlight how the international community can support the Iranian people in achieving a peaceful and democratic transition.

Even under brutal repression, internet shutdowns, and constant threats to life, voices from inside Iran have become more united. Across many cities, citizens are publicly calling for Reza Pahlavi to guide a transitional process, holding placards with his name and image and chanting {SLOGANS_REQUIRED}. These expressions originate within Iran and reflect a growing demand for national unity and a credible alternative to the current regime.

Reza Pahlavi has set out a structured roadmap for transition grounded in democratic principles, human rights, free elections, and the separation of religion and state. He has stated that his role would be to facilitate a transitional period and return decision-making power to the Iranian people through a democratic referendum.

Given the regime’s violence, suppression of independent media, and systematic propaganda, international recognition of the Iranian people’s expressed will is vital. Constructive engagement with a credible transition framework can help deter further repression and support stability beyond Iran’s borders.

Thank you for your time and consideration.

{REFERENCES_BLOCK}""",

    f"""I am writing to express concern over the ongoing situation in Iran and to underscore the importance of international support for a peaceful and democratic transition.

Despite severe repression and internet blackouts, voices from inside Iran are increasingly clear. In many cities, protesters are publicly calling for Reza Pahlavi to guide a transitional process, holding his name and photo while chanting {SLOGANS_REQUIRED}. These calls arise from within Iran and reflect a growing desire for national unity and a credible alternative.

Reza Pahlavi has publicly outlined a clear roadmap for transition grounded in democracy, human rights, free elections, and the separation of religion and state. He has emphasised that his role would be limited to facilitating a transition and returning decision-making power to the Iranian people through a democratic referendum.

Considering the scale of violence, censorship, and propaganda, international recognition of the Iranian people’s expressed will is critically important. Supporting a credible transitional framework can help discourage further repression and contribute to regional and global stability.

Thank you for your time and consideration.

{REFERENCES_BLOCK}""",

    f"""I write concerning the situation in Iran and the role the international community can play in supporting a non-violent and democratic transition.

Even under severe repression and repeated internet shutdowns, voices from inside Iran are increasingly unified. Across many cities, people are publicly calling for Reza Pahlavi to guide a transitional process, holding placards with his name and photo and chanting {SLOGANS_REQUIRED}. These calls originate within Iran and reflect a growing demand for unity and credible leadership.

Reza Pahlavi has presented a structured transition roadmap grounded in democratic principles, human rights, free elections, and the separation of religion and state. He has stated that his role would be to facilitate a transition and return authority to the Iranian people through a democratic referendum.

Given widespread violence, the silencing of independent media, and systematic propaganda, international recognition of these domestic calls is crucial. Constructive engagement with a credible transitional framework can help deter further repression and support stability.

Thank you for your time and consideration.

{REFERENCES_BLOCK}""",

    f"""I am writing to highlight developments inside Iran and the urgent need for international engagement that supports a peaceful and democratic transition.

Despite violent repression, internet shutdowns, and grave risks, voices from inside Iran have become more visible and consistent. In many cities, citizens are calling for Reza Pahlavi to guide a transitional process, holding his image and chanting {SLOGANS_REQUIRED}. These calls are emerging from within Iran itself and reflect a growing demand for national unity and an alternative to the current regime.

Reza Pahlavi has publicly outlined a clear roadmap grounded in democratic principles, human rights, free elections, and the separation of religion and state. He has emphasised that his role would be to facilitate a transitional period and return decision-making power to the Iranian people through a democratic referendum.

In light of ongoing violence, censorship, and propaganda, international recognition of the expressed will of the Iranian people is critically important. Supporting a credible transitional framework can help deter further repression and support stability, both regionally and globally.

Thank you for your time and consideration.

{REFERENCES_BLOCK}""",

   
    f"""I write to respectfully request attention to Iran’s ongoing crisis and the importance of standing with the Iranian people as they seek freedom and democracy.

Even under brutal repression and recurring internet shutdowns, voices from inside Iran are increasingly clear. In many cities, demonstrators are publicly calling for Reza Pahlavi to guide a transitional process, holding placards with his name and photo and chanting {SLOGANS_REQUIRED}. These calls come from within Iran and reflect a growing demand for unity and a credible alternative to the current regime.

Reza Pahlavi has set out a structured roadmap for transition based on democratic principles, human rights, free elections, and the separation of religion and state. He has stated that his role would be temporary and aimed at returning authority to the Iranian people through a democratic referendum.

Given the scale of violence and the systematic suppression of independent media and dissenting voices, international recognition of the Iranian people’s expressed will is crucial. Constructive engagement with a credible transition framework can help deter further repression and contribute to stability.

Thank you for your time and consideration.

{REFERENCES_BLOCK}""",

    f"""I am writing regarding Iran and how the international community can most effectively support a peaceful and democratic transition that reflects the will of the Iranian people.

Despite severe repression, threats to life, and ongoing internet blackouts, calls from inside Iran have become more consistent. Across many cities, citizens are publicly calling for Reza Pahlavi to guide a transitional process, holding his image and chanting {SLOGANS_REQUIRED}. These calls originate within Iran and signal a growing demand for national unity and a credible alternative.

Reza Pahlavi has publicly outlined a clear transition roadmap grounded in democratic principles, human rights, free elections, and the separation of religion and state. He has emphasised that his role would be to facilitate a transition and return decision-making power to the Iranian people through a democratic referendum.

Given ongoing violence, censorship, and propaganda, international recognition of these domestic calls is critically important. Supporting a credible transitional framework can help deter further repression and support regional and global stability.

Thank you for your time and consideration.

{REFERENCES_BLOCK}""",

    f"""I write to draw attention to the situation in Iran and to highlight the need for meaningful international support for a peaceful democratic transition.

Even under severe repression and repeated internet shutdowns, voices from inside Iran have become increasingly clear. In many cities, protesters are publicly calling for Reza Pahlavi to guide a transitional process, holding placards with his name and photo and chanting {SLOGANS_REQUIRED}. These calls are emerging from within Iran and reflect a growing demand for unity and credible leadership.

Reza Pahlavi has outlined a structured roadmap grounded in democracy, human rights, free elections, and the separation of religion and state. He has stated that his role would be to facilitate a transitional period and return power to the Iranian people through a referendum.

Given the scale of violence and the systematic silencing of independent media, international recognition of the Iranian people’s expressed will is vital. Constructive engagement with a credible transitional framework can help deter further repression and support stability.

Thank you for your time and consideration.

{REFERENCES_BLOCK}""",

    f"""I am writing regarding the ongoing crisis in Iran and how the international community can best stand with those seeking freedom and democracy.

Despite brutal repression, internet restrictions, and threats to their lives, voices from inside Iran are increasingly unified. Across many cities, citizens are calling for Reza Pahlavi to guide a transitional process, holding his image and chanting {SLOGANS_REQUIRED}. These calls originate within Iran and reflect a growing demand for national unity and a credible alternative.

Reza Pahlavi has publicly outlined a clear and structured roadmap for transition grounded in democratic principles, human rights, free elections, and the separation of religion and state. He has emphasised that his role would be limited to facilitating a transition and returning decision-making power to the Iranian people through a democratic referendum.

Given ongoing violence, massacres, censorship, and propaganda, international recognition of the Iranian people’s expressed will is critically important. Supporting a credible transitional framework can help deter further repression and contribute to stability.

Thank you for your time and consideration.

{REFERENCES_BLOCK}""",

    f"""I write to raise concern about the situation in Iran and to emphasise the importance of international recognition of the Iranian people’s demands for a peaceful democratic transition.

Even under severe repression and repeated internet blackouts, voices from inside Iran have become clearer. In many cities, people are publicly calling for Reza Pahlavi to guide a transitional process, holding placards with his name and photo and chanting {SLOGANS_REQUIRED}. These calls arise from within Iran and reflect a growing demand for unity and credible leadership.

Reza Pahlavi has presented a structured roadmap grounded in democratic values, human rights, free elections, and the separation of religion and state. He has stated that his role would be to facilitate a transition and return authority to the Iranian people through a democratic referendum.

Given the regime’s violence, censorship, and propaganda, international recognition of the expressed will of Iranians is critically important. Constructive engagement with a credible transition framework can help deter further repression and support stability.

Thank you for your time and consideration.

{REFERENCES_BLOCK}""",

    f"""I am writing to draw attention to the ongoing situation in Iran and the urgent need for international support that advances a peaceful and democratic transition.

Despite severe repression, internet shutdowns, and grave risks, voices from inside Iran have become increasingly consistent. Across many cities, protesters are publicly calling for Reza Pahlavi to guide a transitional process, holding his name and photo while chanting {SLOGANS_REQUIRED}. These calls originate within Iran and reflect a growing demand for national unity and a credible alternative.

Reza Pahlavi has publicly outlined a clear roadmap for transition grounded in democratic principles, human rights, free elections, and the separation of religion and state. He has emphasised that his role would be to facilitate a transitional period and return decision-making power to the Iranian people through a democratic referendum.

In light of widespread violence and systematic suppression of independent media, international recognition of the Iranian people’s expressed will is crucial. Supporting a credible transitional framework can help deter further repression and contribute to regional and global stability.

Thank you for your time and consideration.

{REFERENCES_BLOCK}""",

    f"""I write regarding Iran’s ongoing crisis and how the international community can best support the Iranian people in achieving a peaceful and democratic transition.

Even under brutal repression and repeated internet shutdowns, voices from inside Iran are increasingly clear. Across many cities, citizens are publicly calling for Reza Pahlavi to guide a transitional process, holding placards with his name and photo and chanting {SLOGANS_REQUIRED}. These calls are emerging from within Iran and reflect a growing demand for unity and credible leadership.

Reza Pahlavi has outlined a structured roadmap based on democratic principles, human rights, free elections, and the separation of religion and state. He has stated that his role would be to facilitate a transition and return authority to the people through a democratic referendum.

Given violence, censorship, and propaganda, international recognition of these domestic calls is critically important. Constructive engagement with a credible transition framework can help deter further repression and support stability.

Thank you for your time and consideration.

{REFERENCES_BLOCK}""",

    f"""I am writing about the ongoing situation in Iran and the importance of international recognition of the Iranian people’s calls for a peaceful democratic transition.

Despite severe repression and internet shutdowns, voices from inside Iran have grown more unified. In many cities, demonstrators are calling for Reza Pahlavi to guide a transitional process, holding his image and chanting {SLOGANS_REQUIRED}. These expressions originate within Iran and reflect a growing demand for national unity and a credible alternative.

Reza Pahlavi has publicly outlined a clear and structured roadmap for transition grounded in democratic values, human rights, free elections, and the separation of religion and state. He has emphasised that his role would be temporary and aimed at returning decision-making power to the Iranian people through a democratic referendum.

Given widespread violence and systematic silencing of independent media, international recognition of the expressed will of Iranians is vital. Supporting a credible transitional framework can help deter further repression and contribute to stability.

Thank you for your time and consideration.

{REFERENCES_BLOCK}""",

    f"""I write to request attention to the crisis in Iran and to highlight how the international community can support a peaceful and democratic transition.

Even with severe repression and repeated internet shutdowns, voices from inside Iran are increasingly consistent. Across many cities, people are publicly calling for Reza Pahlavi to guide a transitional process, holding placards with his name and photo and chanting {SLOGANS_REQUIRED}. These calls originate within Iran and reflect a growing demand for unity and credible leadership.

Reza Pahlavi has set out a structured roadmap grounded in democratic principles, human rights, free elections, and the separation of religion and state. He has stated that his role would be to facilitate a transitional period and return authority to the Iranian people through a democratic referendum.

Given the regime’s violence and its systematic suppression of independent media, international recognition of these calls is critically important. Constructive engagement with a credible transition framework can help deter further repression and support stability.

Thank you for your time and consideration.

{REFERENCES_BLOCK}""",

    f"""I am writing regarding the situation in Iran and how the international community can stand with the Iranian people as they seek freedom and a peaceful democratic transition.

Despite brutal repression, internet shutdowns, and risks to life, voices from inside Iran have become increasingly clear. In many cities, citizens are publicly calling for Reza Pahlavi to guide a transitional process, holding his image and chanting {SLOGANS_REQUIRED}. These calls come from within Iran and reflect a growing demand for national unity and a credible alternative.

Reza Pahlavi has publicly outlined a structured roadmap for transition grounded in democratic values, human rights, free elections, and the separation of religion and state. He has emphasised that his role would be limited to facilitating a transition and returning decision-making power to the Iranian people through a democratic referendum.

Given violence, censorship, and propaganda, international recognition of the Iranian people’s expressed will is critically important. Supporting a credible transitional framework can help deter further repression and contribute to regional and global stability.

Thank you for your time and consideration.

{REFERENCES_BLOCK}""",

    f"""I write to underline the urgency of the situation in Iran and the importance of international support for a peaceful and democratic transition.

Despite severe repression and recurring internet shutdowns, voices from inside Iran are increasingly unified. Across many cities, demonstrators are publicly calling for Reza Pahlavi to guide a transitional process, holding placards with his name and photo and chanting {SLOGANS_REQUIRED}. These calls are emerging from within Iran and reflect a growing demand for unity and credible leadership.

Reza Pahlavi has outlined a clear and structured roadmap grounded in democratic principles, human rights, free elections, and the separation of religion and state. He has stated that his role would be to facilitate a transitional period and return decision-making power to the Iranian people through a democratic referendum.

Given the scale of violence and systematic suppression of independent media, international recognition of the Iranian people’s expressed will is crucial. Constructive engagement with a credible transition framework can help deter further repression and support stability.

Thank you for your time and consideration.

{REFERENCES_BLOCK}""",

    f"""I am writing to draw attention to developments inside Iran and the importance of supporting the Iranian people’s pursuit of freedom and democracy.

Even under brutal repression and repeated internet shutdowns, voices from inside Iran have become clearer and more consistent. In many cities, people are publicly calling for Reza Pahlavi to guide a transitional process, holding his photo and chanting {SLOGANS_REQUIRED}. These calls originate within Iran and reflect a growing demand for national unity and a credible alternative.

Reza Pahlavi has publicly outlined a transition roadmap grounded in democratic values, human rights, free elections, and the separation of religion and state. He has emphasised that his role would be limited to facilitating a transition and returning decision-making power to the Iranian people through a democratic referendum.

Given violence, censorship, and propaganda, international recognition of the expressed will of Iranians is critically important. Supporting a credible transitional framework can help deter further repression and contribute to stability regionally and globally.

Thank you for your time and consideration.

{REFERENCES_BLOCK}""",

    f"""I write regarding the ongoing situation in Iran and to stress how the international community can best support a peaceful and democratic transition.

Despite severe repression, internet shutdowns, and threats to life, voices from inside Iran have become increasingly unified. Across many cities, citizens are publicly calling for Reza Pahlavi to guide a transitional process, holding placards with his name and photo and chanting {SLOGANS_REQUIRED}. These expressions originate within Iran and reflect a growing demand for unity and credible leadership.

Reza Pahlavi has outlined a structured roadmap grounded in democracy, human rights, free elections, and separation of religion and state. He has stated that his role would be to facilitate a transitional period and return decision-making power to the Iranian people through a democratic referendum.

Given ongoing violence and systematic silencing of independent media alongside propaganda, international recognition of the expressed will of the Iranian people is vital. Constructive engagement with a credible transition framework can help deter further repression and support stability.

Thank you for your time and consideration.

{REFERENCES_BLOCK}""",

    f"""I am writing about the ongoing crisis in Iran and the importance of international recognition of the Iranian people’s calls for democratic change.

Even under brutal repression and internet shutdowns, voices from inside Iran are increasingly clear. In many cities, demonstrators are publicly calling for Reza Pahlavi to guide a transitional process, holding his name and photo while chanting {SLOGANS_REQUIRED}. These calls emerge from within Iran itself and reflect a growing demand for national unity and a credible alternative.

Reza Pahlavi has publicly presented a clear roadmap grounded in democratic principles, human rights, free elections, and the separation of religion and state. He has emphasised that his role would be temporary and focused on returning decision-making power to the people through a democratic referendum.

Given violence, massacres, censorship, and propaganda, international recognition of the Iranian people’s expressed will is critically important. Supporting a credible transitional framework can help deter further repression and contribute to stability.

Thank you for your time and consideration.

{REFERENCES_BLOCK}""",

    f"""I write to request attention to Iran’s ongoing crisis and to highlight how international engagement can support a peaceful democratic transition.

Despite severe repression and repeated internet shutdowns, voices from inside Iran have become more consistent. Across many cities, citizens are publicly calling for Reza Pahlavi to guide a transitional process, holding placards with his name and photo and chanting {SLOGANS_REQUIRED}. These calls come from within Iran and reflect a growing demand for national unity and credible leadership.

Reza Pahlavi has outlined a structured roadmap grounded in democratic values, human rights, free elections, and the separation of religion and state. He has stated that his role would be to facilitate a transition and return authority to the Iranian people through a democratic referendum.

Given the regime’s violence and systematic silencing of independent media, international recognition of the expressed will of Iranians is vital. Constructive engagement with a credible transition framework can help deter further repression and support stability.

Thank you for your time and consideration.

{REFERENCES_BLOCK}""",

    f"""I am writing regarding the situation in Iran and how the international community can best support the Iranian people’s pursuit of freedom and democratic governance.

Even with severe repression, internet shutdowns, and threats to life, voices from inside Iran have become increasingly clear. In many cities, people are publicly calling for Reza Pahlavi to guide a transitional process, holding his image and chanting {SLOGANS_REQUIRED}. These calls originate within Iran and reflect a growing demand for unity and a credible alternative.

Reza Pahlavi has publicly outlined a clear roadmap grounded in democratic principles, human rights, free elections, and the separation of religion and state. He has emphasised that his role would be to facilitate a transitional period and return decision-making power to the Iranian people through a democratic referendum.

Given ongoing violence, censorship, and propaganda, international recognition of these domestic calls is critically important. Supporting a credible transitional framework can help deter further repression and contribute to regional and global stability.

Thank you for your time and consideration.

{REFERENCES_BLOCK}""",
]


# ---------------------------
# Subject options (rotates)
# ---------------------------
SUBJECT_OPTIONS = [
    "Iran: Recognition of Reza Pahlavi as a Transitional Leader",
    "Iran: Supporting Reza Pahlavi’s Roadmap for Democratic Transition",
    "Iran: Responding to the Iranian People’s Call for Reza Pahlavi",
    "Iran: Engagement with Reza Pahlavi’s Transitional Framework",
    "Iran: Supporting a Peaceful Transition Led by Reza Pahlavi",
    "Iran: Recognition of Reza Pahlavi’s Role in Democratic Transition",
    "Iran: Supporting Reza Pahlavi as a Transitional Leader Chosen by the People",
    "Iran: Reza Pahlavi and a Credible Path to Democratic Transition",
    "Iran: Recognition of Reza Pahlavi’s Transitional Leadership"
]



# ---------------------------
# Helpers: recipients
# ---------------------------
def find_email_column(df: pd.DataFrame) -> str | None:
    candidates = ["email", "Email", "EMAIL", "e-mail", "E-mail", "mail", "Mail"]
    for c in candidates:
        if c in df.columns:
            return c
    for c in df.columns:
        if "email" in str(c).lower():
            return c
    return None


def load_recipients(csv_path: Path) -> list[str]:
    if not csv_path.exists():
        raise FileNotFoundError(
            f"Missing required file: {csv_path.name}. Place it in the same folder as this app."
        )

    df = pd.read_csv(csv_path)
    email_col = find_email_column(df)
    if not email_col:
        raise ValueError("Could not find an email column in the CSV. Please ensure it has a column named 'email'.")

    emails = (
        df[email_col]
        .astype(str)
        .str.strip()
        .replace({"nan": "", "None": ""})
        .tolist()
    )

    seen = set()
    cleaned = []
    for e in emails:
        if not e:
            continue
        if "@" not in e:
            continue
        if e not in seen:
            cleaned.append(e)
            seen.add(e)

    if not cleaned:
        raise ValueError("No valid email addresses were found in the CSV.")
    return cleaned


# ---------------------------
# Helpers: template choice (different from last)
# ---------------------------
def pick_new_index(exclude_index: int | None, n: int) -> int:
    if n <= 1:
        return 0
    choices = list(range(n))
    if exclude_index is not None and exclude_index in choices:
        choices.remove(exclude_index)
    return random.choice(choices)


# ---------------------------
# Helpers: build mailto 
# ---------------------------
def build_mailto_bcc_link(bcc_emails: list[str], subject: str, body: str) -> str:
    bcc_value = ",".join(bcc_emails)
    params = {"bcc": bcc_value, "subject": subject, "body": body}
    query = "&".join(f"{k}={urllib.parse.quote(v, safe='')}" for k, v in params.items())
    return f"mailto:?{query}"


# ---------------------------
# Load recipients
# ---------------------------
try:
    recipients = load_recipients(CSV_PATH)
except Exception as e:
    st.error(str(e))
    st.stop()


# ---------------------------
# Session state
# ---------------------------
if "last_pick" not in st.session_state:
    st.session_state.last_pick = None

if "mailto_url" not in st.session_state:
    st.session_state.mailto_url = None


# ---------------------------
# UI
# ---------------------------
name = st.text_input("Your name (English)")

# Greeting

greeting = "Dear Senator/Member of Parliament,"

if st.button("Step 1: Generate draft email", use_container_width=True):
    if not name.strip():
        st.warning("Please enter your name first.")
    else:
        new_pick = pick_new_index(st.session_state.last_pick, len(EMAIL_TEMPLATES))
        st.session_state.last_pick = new_pick

        subject = SUBJECT_OPTIONS[new_pick % len(SUBJECT_OPTIONS)]
        signoff = f"Sincerely,\n{name.strip()}"

        body_only = EMAIL_TEMPLATES[new_pick]
        full_body = f"{greeting}\n\n{body_only}\n\n{signoff}"

        st.session_state.mailto_url = build_mailto_bcc_link(recipients, subject, full_body)

if st.session_state.mailto_url:
    st.link_button("Step 2: Open email in your email app", st.session_state.mailto_url, use_container_width=True)

st.caption(
    "Note: This tool opens a draft email in your email app with all recipients included in BCC. "
    "The photo album and YouTube references are included as clickable links in the email body."
)

# ---------------------------
# Run command (Terminal)
# ---------------------------
# streamlit run app.py
