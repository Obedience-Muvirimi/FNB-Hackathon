import streamlit as st

# --- 1. MULTI-LANGUAGE DICTIONARY ---
TRANSLATIONS = {
    "English": {
        "title": "💡 FinAdvisor",
        "subtitle": "Smart Income-to-Income Budgeting",
        "desc": "Plan your cash window, protect your essentials, lock in your 20% savings, and pace your spending safely.",
        "step1": "Step 1: Your Job & Timeline",
        "income": "How much did you earn from this job/payout? (ZAR)",
        "days": "How many days until your next expected job or payday?",
        "step2": "Step 2: Essential Expenses",
        "transport": "Transport / Commute Cost (ZAR)",
        "food": "Food & Groceries (ZAR)",
        "utils": "Utilities / Airtime / Data (ZAR)",
        "button": "Calculate My Financial Plan",
        "breakdown": "📊 Your FinAdvisor Breakdown",
        "warn_debt": "⚠️ Your essential expenses exceed your income! Try reducing some non-urgent costs.",
        "tot_exp": "Total Expenses (Needs)",
        "remain": "Remaining Cash",
        "save_target": "🔒 20% Savings Target",
        "daily_limit": "📅 Safe Daily Spend Limit",
        "health": "🚦 Spending Health",
        "tight": "⚠️ Tight Budget: Watch out for non-essential spending!",
        "good": "✅ Healthy Pace: Comfortable daily safety buffer.",
        "advice_title": "💡 Tailored Financial Advice",
        "tip1": "Immediately ring-fence R{transport} for transport so you never miss a shift.",
        "tip2": "Transfer your R{savings} savings into a separate digital pocket or low-fee account so it's out of reach."
    },
    "isiZulu": {
        "title": "💡 FinAdvisor",
        "subtitle": "Ukuhlela Imali Ngobuhlakani",
        "desc": "Hlela isikhathi sakho semali, vikela izidingo zakho, gcina u-20% wakho, futhi usebenzise imali ngokuqapha.",
        "step1": "Isinyathelo 1: Umsebenzi Wakho Nesikhathi",
        "income": "Uhola malini kulo msebenzi? (ZAR)",
        "days": "Zingaki izinsuku kuze kube iholo elilandelayo?",
        "step2": "Isinyathelo 2: Izindleko Ezibalulekile",
        "transport": "Ezezithuthi / Imali yokugibela (ZAR)",
        "food": "Ukudla (ZAR)",
        "utils": "Ugesi / Amanzi / I-Airtime (ZAR)",
        "button": "Bala Uhlelo Lwami Lwemali",
        "breakdown": "📊 Uhla Lwakho Lwe-FinAdvisor",
        "warn_debt": "⚠️ Izindleko zakho zingaphezu kweholo lakho! Zama ukunciphisa izindleko.",
        "tot_exp": "Isamba Sezindleko (Izidingo)",
        "remain": "Imali Esele",
        "save_target": "🔒 Imali Yokonga (20%)",
        "daily_limit": "📅 Imali Yansuku Zonke Ephephile",
        "health": "🚦 Impilo Yokusebenzisa Imali",
        "tight": "⚠️ Ibhagethi Eqinile: Qaphela ukuthenga okungadingekile!",
        "good": "✅ Kulungile: Unemali eyanele yokuzivikela nsuku zonke.",
        "advice_title": "💡 Izeluleko Zemali Zakho",
        "tip1": "Beka eceleni u-R{transport} wemali yokugibela kuqala ukuze ungaphuthelwa umsebenzi.",
        "tip2": "Dlulisa u-R{savings} wakho wokonga kwi-akhawunti ehlukile ngokushesha ukuze ungayisebenzisi."
    },
    "isiXhosa": {
        "title": "💡 FinAdvisor",
        "subtitle": "Ucwangciso Lwemali Olukrelekrele",
        "desc": "Cwangcisa ixesha lakho lemali, khusela iimfuno zakho, gcina i-20% yakho, kwaye uchithe ngokukhuselekileyo.",
        "step1": "Inyathelo 1: Umsebenzi Wakho Nexesha",
        "income": "Ufumene malini kulo msebenzi? (ZAR)",
        "days": "Zingaphi iintsuku kude kube ngumvuzo olandelayo?",
        "step2": "Inyathelo 2: Iindleko Ezibalulekileyo",
        "transport": "Ezezithuthi / Imali yokukhwela (ZAR)",
        "food": "Ukutya (ZAR)",
        "utils": "Umbane / Amanzi / I-Airtime (ZAR)",
        "button": "Bala Ucwangciso Lwam Lwemali",
        "breakdown": "📊 Ingxelo Yakho ye-FinAdvisor",
        "warn_debt": "⚠️ Iindleko zakho zingaphezulu kunomvuzo wakho! Zama ukunciphisa iindleko.",
        "tot_exp": "Umgangatho Weendleko",
        "remain": "Imali Eseleyo",
        "save_target": "🔒 Imali Yokugcina (20%)",
        "daily_limit": "📅 Imali Yemihla Ngemihla Ekhuselekileyo",
        "health": "🚦 Impilo Yokusebenzisa Imali",
        "tight": "⚠️ Uhlahlo-lwabiwo mali oluqinileyo: Lumkela inkcitho engeyomfuneko!",
        "good": "✅ Ikhuselekile: Unemali eyaneleyo yemihla ngemihla.",
        "advice_title": "💡 Iingcebiso Zemali Zakho",
        "tip1": "Beka bucala u-R{transport} wezithuthi kuqala ukuze ungaphoswa ngumsebenzi.",
        "tip2": "Dlulisa u-R{savings} wakho wokugcina kwi-akhawunti eyahlukileyo ngoko nangoko."
    },
    "Afrikaans": {
        "title": "💡 FinAdvisor",
        "subtitle": "Slim Inkomste-tot-Inkomste Begroting",
        "desc": "Beplan jou kontant, beskerm jou noodsaaklikhede, sluit jou 20% spaargeld toe, en spandeer veilig.",
        "step1": "Stap 1: Jou Werk & Tydlyn",
        "income": "Hoeveel het jy verdien van hierdie werk? (ZAR)",
        "days": "Hoeveel dae tot jou volgende verwagte betaaldag?",
        "step2": "Stap 2: Noodsaaklike Uitgawes",
        "transport": "Vervoer Koste (ZAR)",
        "food": "Kos & Kruideniersware (ZAR)",
        "utils": "Krag / Lugtyd / Data (ZAR)",
        "button": "Bereken My Finansiële Plan",
        "breakdown": "📊 Jou FinAdvisor Opsomming",
        "warn_debt": "⚠️ Jou uitgawes oorskry jou inkomste! Probeer kostes besnoei.",
        "tot_exp": "Totale Uitgawes (Behoeftes)",
        "remain": "Oorblywende Kontant",
        "save_target": "🔒 20% Spaar Teiken",
        "daily_limit": "📅 Veilige Daaglikse Toelae",
        "health": "🚦 Spanderings Gesondheid",
        "tight": "⚠️ Streng Begroting: Pasop vir onnodige uitgawes!",
        "good": "✅ Gesonde Pas: Gemaklike daaglikse veiligheidsbuffer.",
        "advice_title": "💡 Gepersonaliseerde Finansiële Advies",
        "tip1": "Sit jou R{transport} vervoergeld eerste opsy sodat jy nooit 'n skof mis nie.",
        "tip2": "Plaas jou R{savings} spaargeld onmiddellik in 'n aparte rekening sodat jy dit nie spandeer nie."
    },
    "Sesotho": {
        "title": "💡 FinAdvisor",
        "subtitle": "Tekanyetso e Bohlale ya Tjhelete",
        "desc": "Rera nako ya tjhelete ya hao, sireletsa ditshenyehelo tsa hao, boloka 20%, mme o sebedise ka polokeho.",
        "step1": "Mohato wa 1: Mosebetsi wa Hao le Nako",
        "income": "O fumane bokae mosebetsing ona? (ZAR)",
        "days": "Ho setse matsatsi a makae pele ho moputso o latelang?",
        "step2": "Mohato wa 2: Ditshenyehelo Tsa Bohlokwa",
        "transport": "Dipalangwang (ZAR)",
        "food": "Dijo (ZAR)",
        "utils": "Motlakase / Airtime (ZAR)",
        "button": "Bala Leano la Ka la Tjhelete",
        "breakdown": "📊 Tlhaloso ya Hao ya FinAdvisor",
        "warn_debt": "⚠️ Ditshenyehelo tsa hao di feta moputso wa hao! Leka ho fokotsa ditshenyehelo.",
        "tot_exp": "Paloyohle ya Ditshenyehelo",
        "remain": "Tjhelete e Setseng",
        "save_target": "🔒 Tjhelete ya ho Boloka (20%)",
        "daily_limit": "📅 Tjhelete ya Letsatsi e Bolokehileng",
        "health": "🚦 Bophelo ba ho Sebedisa Tjhelete",
        "tight": "⚠️ Tekanyetso e Tlepane: Hlokomela ditshenyehelo tse sa hlokahaleng!",
        "good": "✅ Ho Lokile: O na le tjhelete e lekaneng ya letsatsi.",
        "advice_title": "💡 Dikeletso Tsa Tjhelete Tsa Hao",
        "tip1": "Behela R{transport} ya dipalangwang ka thoko pele ho tsohle.",
        "tip2": "Fetisetsa R{savings} ya hao ya poloko akhaonteng e fapaneng hona jwale."
    }
}

# --- 2. APP CONFIGURATION & UI ---
st.set_page_config(page_title="FinAdvisor", page_icon="💡", layout="centered")

# Language Selector
selected_lang = st.selectbox("🌐 Select Language / Khetha Ulimi / Kies Taal / Kgetha Puo:", 
                             ["English", "isiZulu", "isiXhosa", "Afrikaans", "Sesotho"])
t = TRANSLATIONS[selected_lang]

# Headers
st.title(t["title"])
st.subheader(t["subtitle"])
st.write(t["desc"])
st.divider()

# Inputs
st.markdown(f"### {t['step1']}")
income = st.number_input(t["income"], min_value=0.0, value=1500.0, step=50.0)
days = st.number_input(t["days"], min_value=1, value=10, step=1)

st.markdown(f"### {t['step2']}")
transport = st.number_input(t["transport"], min_value=0.0, value=400.0, step=10.0)
food = st.number_input(t["food"], min_value=0.0, value=0.0, step=10.0)
utilities = st.number_input(t["utils"], min_value=0.0, value=0.0, step=10.0)

# --- 3. CALCULATIONS & DASHBOARD ---
if st.button(t["button"], type="primary"):
    total_expenses = transport + food + utilities
    remaining_cash = income - total_expenses

    st.divider()
    st.markdown(f"### {t['breakdown']}")

    if remaining_cash < 0:
        st.error(t["warn_debt"])
    else:
        # Calculate 20% savings rule & daily pace
        savings_target = remaining_cash * 0.20
        spendable_cash = remaining_cash - savings_target
        daily_allowance = spendable_cash / days if days > 0 else 0

        # Layout metrics in a nice 2x2 grid
        col1, col2 = st.columns(2)
        with col1:
            st.metric(label=t["tot_exp"], value=f"R{total_expenses:.2f}")
            st.metric(label=t["remain"], value=f"R{remaining_cash:.2f}")
        with col2:
            st.metric(label=t["save_target"], value=f"R{savings_target:.2f}")
            st.metric(label=t["daily_limit"], value=f"R{daily_allowance:.2f} / day")

        # Visual Health Indicator
        st.markdown(f"### {t['health']}")
        if daily_allowance < 50:
            st.warning(t["tight"])
        else:
            st.success(t["good"])

        # Contextual Advice
        st.markdown(f"### {t['advice_title']}")
        st.info(f"**1.** {t['tip1'].format(transport=transport)}")
        st.info(f"**2.** {t['tip2'].format(savings=savings_target)}")