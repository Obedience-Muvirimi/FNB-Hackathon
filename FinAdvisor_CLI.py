def get_translations():
    # Dictionary containing all language translations
    return {
        "1": {
            "name": "English",
            "welcome": "Welcome to FinAdvisor: Smart Income-to-Income Budgeting",
            "income": "Enter how much you earned from this job / payout (ZAR): R",
            "days": "How many days until your next expected job or payday?: ",
            "expenses_head": "--- Enter Your Essential Expenses for This Period ---",
            "transport": "Transport / Commute Cost (ZAR): R",
            "food": "Food & Groceries (ZAR): R",
            "utils": "Utilities / Airtime / Data (ZAR): R",
            "breakdown": "YOUR FINADVISOR BREAKDOWN",
            "warning_debt": "WARNING: Your essential expenses exceed your income! Try reducing costs.",
            "tot_income": "Total Income:",
            "tot_expense": "Total Expenses (Needs):",
            "remain": "Remaining Balance:",
            "savings": "20% Savings Target:",
            "daily": "Safe Daily Allowance:",
            "tight": "SPENDING HEALTH: TIGHT BUDGET - Watch out for non-essential spending!",
            "healthy": "SPENDING HEALTH: HEALTHY PACE - Comfortable safety buffer.",
            "advice": "TAILORED FINANCIAL ADVICE",
            "tip1": "1. Ring-fence your transport money first so you never miss a shift.",
            "tip2": "2. Transfer your 20% savings into a separate account immediately.",
            "error": "Invalid input! Please enter numbers only."
        },
        "2": {
            "name": "isiZulu",
            "welcome": "Siyakwamukela ku-FinAdvisor: Ukuhlela Imali Ngobuhlakani",
            "income": "Faka inani oyiholile kulo msebenzi (ZAR): R",
            "days": "Zingaki izinsuku kuze kube iholo elilandelayo?: ",
            "expenses_head": "--- Faka Izindleko Zakho Ezibalulekile ---",
            "transport": "Ezezithuthi / Imali yokugibela (ZAR): R",
            "food": "Ukudla (ZAR): R",
            "utils": "Ugesi / Amanzi / I-Airtime (ZAR): R",
            "breakdown": "UHLA LWAKHO LWE-FINADVISOR",
            "warning_debt": "ISEXWAYISO: Izindleko zakho zingaphezu kweholo lakho! Zama ukunciphisa izindleko.",
            "tot_income": "Isamba Semali Engenayo:",
            "tot_expense": "Isamba Sezindleko (Izidingo):",
            "remain": "Imali Esele:",
            "savings": "Imali Yokonga (20%):",
            "daily": "Imali Yansuku Zonke Ephephile:",
            "tight": "IMPILO YOKUSEBENZISA IMALI: IBHAGETHI EQINILE - Qaphela ukuthenga okungadingekile!",
            "healthy": "IMPILO YOKUSEBENZISA IMALI: KULUNGILE - Unemali eyanele yokuzivikela.",
            "advice": "IZELULEKO ZEMALI ZAKHO",
            "tip1": "1. Beka eceleni imali yokugibela kuqala ukuze ungaphuthelwa umsebenzi.",
            "tip2": "2. Dlulisa u-20% wakho wokonga kwi-akhawunti ehlukile ngokushesha.",
            "error": "Iphutha! Sicela ufake izinombolo kuphela."
        },
        "3": {
            "name": "isiXhosa",
            "welcome": "Wamkelekile kwi-FinAdvisor: Ucwangciso Lwemali Olukrelekrele",
            "income": "Faka isixa osifumeneyo kulo msebenzi (ZAR): R",
            "days": "Zingaphi iintsuku kude kube ngumvuzo olandelayo?: ",
            "expenses_head": "--- Faka Iindleko Zakho Ezibalulekileyo ---",
            "transport": "Ezezithuthi / Imali yokukhwela (ZAR): R",
            "food": "Ukutya (ZAR): R",
            "utils": "Umbane / Amanzi / I-Airtime (ZAR): R",
            "breakdown": "INGXELO YAKHO YE-FINADVISOR",
            "warning_debt": "ISILUMKISO: Iindleko zakho zingaphezulu kunomvuzo wakho! Zama ukunciphisa iindleko.",
            "tot_income": "Umgangatho Wemali Engenayo:",
            "tot_expense": "Umgangatho Weendleko:",
            "remain": "Imali Eseleyo:",
            "savings": "Imali Yokugcina (20%):",
            "daily": "Imali Yemihla Ngemihla Ekhuselekileyo:",
            "tight": "IMPILO YOKUSEBENZISA IMALI: UHLAHLO-LWABIWO MALI OLUQINILEyo - Lumkela inkcitho engeyomfuneko!",
            "healthy": "IMPILO YOKUSEBENZISA IMALI: IKHUSELEKILE - Unemali eyaneleyo.",
            "advice": "IINGCEBISO ZEMALI ZAKHO",
            "tip1": "1. Beka bucala imali yezithuthi kuqala ukuze ungaphoswa ngumsebenzi.",
            "tip2": "2. Dlulisa i-20% yakho yokugcina kwi-akhawunti eyahlukileyo ngoko nangoko.",
            "error": "Impazamo! Nceda ufake amanani kuphela."
        },
        "4": {
            "name": "Afrikaans",
            "welcome": "Welkom by FinAdvisor: Slim Inkomste-tot-Inkomste Begroting",
            "income": "Voer in hoeveel jy verdien het van hierdie werk (ZAR): R",
            "days": "Hoeveel dae tot jou volgende verwagte betaaldag?: ",
            "expenses_head": "--- Voer Jou Noodsaaklike Uitgawes In ---",
            "transport": "Vervoer Koste (ZAR): R",
            "food": "Kos & Kruideniersware (ZAR): R",
            "utils": "Krag / Lugtyd / Data (ZAR): R",
            "breakdown": "JOU FINADVISOR OPSOMMING",
            "warning_debt": "WAARSKUWING: Jou uitgawes oorskry jou inkomste! Probeer kostes besnoei.",
            "tot_income": "Totale Inkomste:",
            "tot_expense": "Totale Uitgawes (Behoeftes):",
            "remain": "Oorblywende Balans:",
            "savings": "20% Spaar Teiken:",
            "daily": "Veilige Daaglikse Toelae:",
            "tight": "SPANDERINGS GESONDHEID: STRENG BEGROTING - Pasop vir onnodige uitgawes!",
            "healthy": "SPANDERINGS GESONDHEID: GESONDE PAS - Gemaklike veiligheidsbuffer.",
            "advice": "GEPERSONALISEERDE FINANSIËLE ADVIES",
            "tip1": "1. Sit jou vervoergeld eerste opsy sodat jy nooit 'n skof mis nie.",
            "tip2": "2. Plaas jou 20% spaargeld onmiddellik in 'n aparte rekening.",
            "error": "Ongeldige inset! Voer asseblief slegs syfers in."
        },
        "5": {
            "name": "Sesotho",
            "welcome": "Rea o amohela ho FinAdvisor: Tekanyetso e Bohlale ya Tjhelete",
            "income": "Kenya hore na o fumane bokae mosebetsing ona (ZAR): R",
            "days": "Ho setse matsatsi a makae pele ho moputso o latelang?: ",
            "expenses_head": "--- Kenya Ditshenyehelo Tsa Hao Tsa Bohlokwa ---",
            "transport": "Dipalangwang (ZAR): R",
            "food": "Dijo (ZAR): R",
            "utils": "Motlakase / Airtime (ZAR): R",
            "breakdown": "TLHALOSO YA HAO YA FINADVISOR",
            "warning_debt": "TEMOSO: Ditshenyehelo tsa hao di feta moputso wa hao! Leka ho fokotsa ditshenyehelo.",
            "tot_income": "Paloyohle ya Tjhelete e Kenang:",
            "tot_expense": "Paloyohle ya Ditshenyehelo:",
            "remain": "Tjhelete e Setseng:",
            "savings": "Tjhelete ya ho Boloka (20%):",
            "daily": "Tjhelete ya Letsatsi e Bolokehileng:",
            "tight": "BOPHELO BA HO SEBEDISA TJHELETE: TEKANYETSO E TLEPANE - Hlokomela ditshenyehelo tse sa hlokahaleng!",
            "healthy": "BOPHELO BA HO SEBEDISA TJHELETE: HO LOKILE - O na le tjhelete e lekaneng.",
            "advice": "DIKELETSO TSA TJHELETE TSA HAO",
            "tip1": "1. Behela tjhelete ya dipalangwang ka thoko pele ho tsohle.",
            "tip2": "2. Fetisetsa 20% ya hao ya poloko akhaonteng e fapaneng hona jwale.",
            "error": "Phoso! Ka kopo kenya dinomoro fela."
        }
        # To add Setswana, Xitsonga, Tshivenda, siSwati, isiNdebele, and Sepedi, 
        # simply copy the block above, change the number to "6", "7", etc., and translate the strings!
    }

def finadvisor_app():
    langs = get_translations()
    
    print("=" * 60)
    print("Choose your language / Khetha Ulimi / Kies Taal / Kgetha Puo:")
    for key, data in langs.items():
        print(f"{key}. {data['name']}")
    print("=" * 60)
    
    choice = input("Enter number (1-5): ")
    if choice not in langs:
        choice = "1" # Default to English if invalid choice
        print("Defaulting to English...\n")
        
    t = langs[choice]

    print("\n" + "=" * 60)
    print(t["welcome"])
    print("=" * 60 + "\n")

    try:
        income = float(input(t["income"]))
        days = int(input(t["days"]))
        
        print("\n" + t["expenses_head"])
        transport = float(input(t["transport"]))
        food = float(input(t["food"]))
        utilities = float(input(t["utils"]))

        total_expenses = transport + food + utilities
        remaining_cash = income - total_expenses

        print("\n" + "=" * 60)
        print(t["breakdown"])
        print("=" * 60)

        if remaining_cash < 0:
            print(t["warning_debt"])
        else:
            savings_target = remaining_cash * 0.20
            spendable_cash = remaining_cash - savings_target
            daily_allowance = spendable_cash / days if days > 0 else 0

            print(f"{t['tot_income']:<30} R{income:.2f}")
            print(f"{t['tot_expense']:<30} R{total_expenses:.2f}")
            print(f"{t['remain']:<30} R{remaining_cash:.2f}")
            print("-" * 40)
            print(f"{t['savings']:<30} R{savings_target:.2f}")
            print(f"{t['daily']:<30} R{daily_allowance:.2f} (for {days} days)")
            print("-" * 40)

            if daily_allowance < 50:
                print(t["tight"])
            else:
                print(t["healthy"])

            print("\n" + "=" * 60)
            print(t["advice"])
            print("=" * 60)
            print(t["tip1"])
            print(t["tip2"])

    except ValueError:
        print("\n" + t["error"])

    print("\n" + "=" * 60)

if __name__ == "__main__":
    finadvisor_app()