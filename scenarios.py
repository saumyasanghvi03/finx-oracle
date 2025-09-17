# scenarios.py

SCENARIOS = [
    # --- Fintech Questions (20) ---
    {
        "title": "Fintech: Central Bank Digital Currencies (CBDCs)",
        "description": "*Global Mini Highlight: India's Digital Rupee and China's Digital Yuan have seen significant retail adoption by late 2025.*\n\nWhat are two key differences between a government-issued CBDC and a decentralized cryptocurrency like Bitcoin?",
        "category": "fintech",
        "references": "- **Concept:** [CBDC](https://www.investopedia.com/terms/c/central-bank-digital-currency-cbdc.asp)",
        "choices": [
            {"text": "A CBDC is centralized and controlled by a central bank.", "correct": True, "feedback": "Correct. CBDCs are a government liability, unlike decentralized cryptocurrencies."},
            {"text": "A CBDC's value is pegged to the national fiat currency.", "correct": True, "feedback": "Correct. One Digital Rupee is worth one physical Rupee, whereas Bitcoin's value floats freely."},
            {"text": "Only Bitcoin uses blockchain technology.", "correct": False, "feedback": "Incorrect. CBDCs also use distributed ledger technology, though it is often a private, permissioned version."},
            {"text": "A CBDC is completely anonymous.", "correct": False, "feedback": "Incorrect. CBDCs are designed with regulatory compliance in mind and would not be anonymous."}
        ]
    },
    {
        "title": "Fintech: AI in Trading",
        "description": "*Global Mini Highlight: A 2025 report shows over 70% of institutional trades are now executed by AI-driven algorithms.*\n\nWhat are two primary risks of relying heavily on AI in financial markets?",
        "category": "fintech",
        "references": "- **Risk:** [Algorithmic Trading Risks](https://www.investopedia.com/articles/active-trading/101014/basics-algorithmic-trading-concepts-and-examples.asp)",
        "choices": [
            {"text": "The potential for 'flash crashes' caused by rapid, automated feedback loops.", "correct": True, "feedback": "Correct. If multiple AIs react to the same data in the same way, they can amplify market moves dangerously fast."},
            {"text": "'Model decay,' where an AI's strategy becomes obsolete as market conditions change.", "correct": True, "feedback": "Correct. A model trained on past data may not be effective in a new market regime, leading to losses."},
            {"text": "AI algorithms guarantee higher returns than human traders.", "correct": False, "feedback": "Incorrect. AIs are tools and carry their own risks; they do not guarantee superior performance."},
            {"text": "Regulators have banned the use of AI in all public markets.", "correct": False, "feedback": "Incorrect. AI is widely used and regulated, not banned."}
        ]
    },
    {
        "title": "Fintech: Tokenization of Real-World Assets",
        "description": "*Global Mini Highlight: A landmark deal in 2025 saw a major commercial real estate portfolio in Mumbai tokenized on a public blockchain.*\n\nWhat are two main benefits of tokenizing a real-world asset like a building?",
        "category": "fintech",
        "references": "- **Concept:** [Tokenization](https://www.investopedia.com/terms/t/tokenization.asp)",
        "choices": [
            {"text": "It increases liquidity by making the asset easier to trade 24/7.", "correct": True, "feedback": "Correct. Tokens can be traded on digital exchanges, unlike a physical building which can take months to sell."},
            {"text": "It enables fractional ownership, allowing smaller investors to participate.", "correct": True, "feedback": "Correct. A multi-crore property can be divided into thousands of affordable tokens."},
            {"text": "It eliminates the need to pay property taxes on the building.", "correct": False, "feedback": "Incorrect. The underlying asset is still subject to all relevant laws and taxes."},
            {"text": "It makes the physical building immune to damage.", "correct": False, "feedback": "Incorrect. Tokenization represents ownership digitally; it does not protect the physical asset itself."}
        ]
    },
    {
        "title": "Fintech: Decentralized Finance (DeFi) Regulation",
        "description": "*Global Mini Highlight: Following several major protocol collapses in 2024, global regulators introduced the 'DeFi Framework' in 2025.*\n\nWhat are two common areas of focus for DeFi regulation?",
        "category": "fintech",
        "references": "- **Topic:** [DeFi Regulation](https://www.investopedia.com/decentralized-finance-defi-5113835)",
        "choices": [
            {"text": "Implementing Anti-Money Laundering (AML) and Know Your Customer (KYC) rules.", "correct": True, "feedback": "Correct. Regulators want to prevent illicit activities on these platforms."},
            {"text": "Ensuring stablecoins are fully backed by legitimate reserves.", "correct": True, "feedback": "Correct. The stability of the ecosystem's core assets is a major concern for regulators."},
            {"text": "Banning the use of all cryptocurrencies.", "correct": False, "feedback": "Incorrect. Regulation aims to manage risks and integrate DeFi into the financial system, not ban it outright."},
            {"text": "Forcing all DeFi protocols to be run by governments.", "correct": False, "feedback": "Incorrect. The goal is to regulate the protocols, not for governments to operate them."}
        ]
    },
    {
        "title": "Fintech: Embedded Finance",
        "description": "*Global Mini Highlight: By 2025, it's common to get insurance or loans directly within non-financial apps like ride-sharing or e-commerce platforms.*\n\nWhat are two examples of 'Embedded Finance'?",
        "category": "fintech",
        "references": "- **Concept:** [Embedded Finance](https://www.forbes.com/advisor/banking/what-is-embedded-finance/)",
        "choices": [
            {"text": "Getting a loan directly from an e-commerce website's checkout page.", "correct": True, "feedback": "Correct. This embeds the financing process directly into the non-financial journey of online shopping."},
            {"text": "Buying travel insurance as an add-on when booking a flight online.", "correct": True, "feedback": "Correct. This embeds the insurance product into the retail experience of travel booking."},
            {"text": "Withdrawing cash from a traditional bank's ATM.", "correct": False, "feedback": "Incorrect. This is a standard banking service, not finance embedded into a non-financial product."},
            {"text": "Applying for a mortgage by physically visiting a bank branch.", "correct": False, "feedback": "Incorrect. This is a traditional financial service, the opposite of the seamless integration of embedded finance."}
        ]
    },
    {
        "title": "Fintech: 'Buy Now, Pay Later' (BNPL)",
        "description": "*Global Mini Highlight: In 2025, regulators in India and Europe have started to classify certain BNPL products as traditional credit.*\n\nWhat are two implications of this regulatory shift?",
        "category": "fintech",
        "references": "- **Concept:** [Buy Now, Pay Later (BNPL)](https://www.investopedia.com/buy-now-pay-later-5182291)",
        "choices": [
            {"text": "BNPL providers may need to conduct more rigorous credit checks on users.", "correct": True, "feedback": "Correct. Being classified as credit often requires stricter affordability checks."},
            {"text": "Users' repayment history with BNPL could start affecting their official credit scores.", "correct": True, "feedback": "Correct. If it's considered a credit product, the data is more likely to be reported to credit bureaus."},
            {"text": "All BNPL services will become completely free for all users.", "correct": False, "feedback": "Incorrect. Regulation typically increases operational costs, not eliminates revenue sources."},
            {"text": "Merchants will no longer be allowed to offer BNPL options.", "correct": False, "feedback": "Incorrect. The regulation focuses on the consumer credit aspect, not banning the service for merchants."}
        ]
    },
    {
        "title": "Fintech: Neobanks",
        "description": "*Global Mini Highlight: By 2025, several digital-only Neobanks have become profitable by focusing on niche markets.*\n\nWhat are two common characteristics of 'Neobanks'?",
        "category": "fintech",
        "references": "- **Business Model:** [Neobank](https://www.investopedia.com/terms/n/neobank.asp)",
        "choices": [
            {"text": "They operate without physical bank branches.", "correct": True, "feedback": "Their digital-only model reduces overhead and costs."},
            {"text": "They typically offer lower fees than traditional banks.", "correct": True, "feedback": "Their lower cost structure allows them to pass savings onto customers with fewer fees."},
            {"text": "They have been in operation for over a century.", "correct": False, "feedback": "Neobanks are a very recent phenomenon, emerging with the rise of smartphones and the internet."},
            {"text": "They focus primarily on providing services to large corporations.", "correct": False, "feedback": "Neobanks are typically focused on retail consumers and small to medium-sized businesses."}
        ]
    },
    {
        "title": "Fintech: Open Banking",
        "description": "*Global Mini Highlight: India's UPI and Account Aggregator framework is a leading example of Open Banking principles in 2025.*\n\nWhat are two key outcomes of 'Open Banking'?",
        "category": "fintech",
        "references": "- **Concept:** [Open Banking](https://www.investopedia.com/terms/o/open-banking.asp)",
        "choices": [
            {"text": "It allows third-party financial apps to access a user's bank data with their consent.", "correct": True, "feedback": "This is the primary mechanism, using secure APIs to share data."},
            {"text": "It fosters greater competition and innovation in financial services.", "correct": True, "feedback": "By allowing new fintech companies to build services on top of bank data, it creates more choices for consumers."},
            {"text": "It merges all of a user's bank accounts into a single government-controlled account.", "correct": False, "feedback": "It's about data sharing with user consent, not consolidation under government control."},
            {"text": "It eliminates the need for passwords by using only biometric authentication.", "correct": False, "feedback": "Open Banking's core function is data sharing via APIs, not changing authentication rules."}
        ]
    },
    {
        "title": "Fintech: Insurtech",
        "description": "*Global Mini Highlight: Parametric insurance, powered by Insurtech, has become a popular product for climate-related risks in 2025.*\n\nWhich two are common applications of 'Insurtech'?",
        "category": "fintech",
        "references": "- **Industry:** [Insurtech](https.www.investopedia.com/terms/i/insurtech.asp)",
        "choices": [
            {"text": "Using telematics data from a car to determine auto insurance premiums.", "correct": True, "feedback": "This is a prime example of using real-time data to price risk more accurately."},
            {"text": "Automating claims processing using AI and photos from a smartphone.", "correct": True, "feedback": "This speeds up the claims process from weeks to minutes for simple cases."},
            {"text": "Replacing all human insurance agents with robots.", "correct": False, "feedback": "While Insurtech automates processes, human agents still play a key role."},
            {"text": "Creating a single insurance policy that covers every possible risk.", "correct": False, "feedback": "Insurtech focuses on personalizing and specializing insurance, not a one-size-fits-all policy."}
        ]
    },
    {
        "title": "Fintech: Staking in Crypto",
        "description": "*Global Mini Highlight: Liquid staking protocols like Lido have become a foundational layer of DeFi by 2025, holding billions in assets.*\n\nIn a Proof-of-Stake (PoS) system, what are two purposes of 'staking'?",
        "category": "fintech",
        "references": "- **Concept:** [Proof-of-Stake (PoS)](https://www.investopedia.com/terms/p/proof-stake-pos.asp)",
        "choices": [
            {"text": "To participate in validating transactions and securing the network.", "correct": True, "feedback": "This is the core function; stakers act as validators for the blockchain."},
            {"text": "To earn rewards or yield, similar to earning interest.", "correct": True, "feedback": "Validators are compensated for their work with additional tokens, providing a return on the staked assets."},
            {"text": "To hide transactions from the public ledger.", "correct": False, "feedback": "Staking is part of the public validation process; it doesn't hide transactions."},
            {"text": "To convert cryptocurrency into physical cash.", "correct": False, "feedback": "Staking is an on-chain activity and is unrelated to cashing out."}
        ]
    },
    {
        "title": "Fintech: Digital Wallets",
        "description": "*Global Mini Highlight: In 2025, digital wallets in India have expanded to include features like automatic toll payments and integrated metro transit passes.*\n\nWhat are two key features of modern digital wallets?",
        "category": "fintech",
        "references": "- **Technology:** [Digital Wallet](https://www.investopedia.com/terms/d/digital-wallet.asp)",
        "choices": [
            {"text": "They use tokenization to protect actual card numbers during transactions.", "correct": True, "feedback": "Tokenization replaces your sensitive card data with a unique, temporary token for each transaction, enhancing security."},
            {"text": "They enable contactless payments using NFC technology.", "correct": True, "feedback": "Near Field Communication (NFC) allows you to pay by simply tapping your device on a compatible terminal."},
            {"text": "They are required by law to print a paper receipt for every transaction.", "correct": False, "feedback": "Digital wallets are designed to reduce paper and provide digital receipts."},
            {"text": "They can only be used to purchase items from a single brand.", "correct": False, "feedback": "They are designed to be used at a wide variety of merchants who accept contactless payments."}
        ]
    },
    {
        "title": "Fintech: RegTech",
        "description": "*Global Mini Highlight: Banks in 2025 are using RegTech to automate their climate risk disclosure reports, a new regulatory requirement.*\n\nWhat are two primary goals of Regulatory Technology (RegTech)?",
        "category": "fintech",
        "references": "- **Industry:** [RegTech](https://www.investopedia.com/terms/r/regtech.asp)",
        "choices": [
            {"text": "To help financial institutions comply with regulations more efficiently and cheaply.", "correct": True, "feedback": "RegTech automates compliance tasks, reducing manual effort and cost."},
            {"text": "To monitor transactions in real-time to identify potential fraud or money laundering.", "correct": True, "feedback": "Automated monitoring of Anti-Money Laundering (AML) and Know Your Customer (KYC) rules is a core function."},
            {"text": "To help individuals avoid paying taxes.", "correct": False, "feedback": "RegTech is designed to enhance compliance with laws, not to evade them."},
            {"text": "To replace financial regulators like the SEBI with AI.", "correct": False, "feedback": "RegTech is a tool used by companies to comply with regulators, not to replace the regulators themselves."}
        ]
    },
    {
        "title": "Fintech: DAOs",
        "description": "*Global Mini Highlight: A prominent venture capital fund in 2025 restructured into a DAO to allow its portfolio companies a say in governance.*\n\nWhat are two characteristics of a DAO?",
        "category": "fintech",
        "references": "- **Concept:** [DAO](https://www.investopedia.com/decentralized-autonomous-organization-dao-5214422)",
        "choices": [
            {"text": "It is governed by rules encoded as smart contracts on a blockchain.", "correct": True, "feedback": "The rules are transparent and automatically enforced by code."},
            {"text": "Decisions are typically made collectively by the members through voting.", "correct": True, "feedback": "This provides a democratic and decentralized governance structure."},
            {"text": "It has a traditional corporate structure with a CEO and board of directors.", "correct": False, "feedback": "A DAO is designed to be 'flat' and community-governed, replacing the need for a traditional hierarchy."},
            {"text": "It is registered and headquartered in a specific physical country.", "correct": False, "feedback": "DAOs are internet-native organizations that can operate without a physical headquarters or specific jurisdiction."}
        ]
    },
    {
        "title": "Fintech: Stablecoins",
        "description": "*Global Mini Highlight: The circulation of regulated, fully-backed stablecoins surpassed $500 billion in 2025.*\n\nWhat are two primary functions of 'stablecoins' in the crypto ecosystem?",
        "category": "fintech",
        "references": "- **Asset:** [Stablecoin](https://www.investopedia.com/terms/s/stablecoin.asp)",
        "choices": [
            {"text": "To act as a stable store of value, pegged to an asset like the US dollar or Rupee.", "correct": True, "feedback": "This allows crypto traders to avoid volatility without cashing out to fiat."},
            {"text": "To serve as a reliable medium of exchange for trading and DeFi applications.", "correct": True, "feedback": "They are a common unit of account on crypto platforms, making it easier to trade and price digital assets."},
            {"text": "To provide the highest possible investment returns in crypto.", "correct": False, "feedback": "Their goal is stability, not high returns. They are designed to hold a steady value."},
            {"text": "To ensure complete and untraceable anonymity for all transactions.", "correct": False, "feedback": "Major stablecoins like USDC and USDT operate with a high degree of transparency."}
        ]
    },
    {
        "title": "Fintech: AI in Credit Scoring",
        "description": "*Global Mini Highlight: In India, by 2025, many lenders use AI models that analyze alternative data (like utility payments) for credit scoring.*\n\nWhat are two benefits of using AI in credit scoring?",
        "category": "fintech",
        "references": "- **Concept:** [Alternative Data](https://www.investopedia.com/terms/a/alternative-data.asp)",
        "choices": [
            {"text": "It can increase financial inclusion by scoring people without a traditional credit history.", "correct": True, "feedback": "Correct. AI can find patterns in other data to assess creditworthiness for the 'unbanked' or 'underbanked'."},
            {"text": "It can potentially create more accurate and predictive risk models than traditional methods.", "correct": True, "feedback": "Correct. By analyzing more variables, AI can identify subtle patterns of risk that older models might miss."},
            {"text": "It guarantees that no borrower will ever default on a loan.", "correct": False, "feedback": "Incorrect. It aims to better predict the probability of default, but it cannot eliminate the risk entirely."},
            {"text": "It makes all loan applications require a physical interview.", "correct": False, "feedback": "Incorrect. It enables a more automated, digital-first application process."}
        ]
    },
    {
        "title": "Fintech: Cross-Border Payments",
        "description": "*Global Mini Highlight: By 2025, fintech solutions using blockchain have reduced the average cost of international remittances by 40% compared to 2020 levels.*\n\nWhat are two main problems with traditional cross-border payments that fintech aims to solve?",
        "category": "fintech",
        "references": "- **Industry:** [Cross-Border Payments](https://www.forbes.com/advisor/money-transfer/best-ways-to-send-money-internationally/)",
        "choices": [
            {"text": "High fees charged by intermediary banks.", "correct": True, "feedback": "Correct. Traditional systems like SWIFT involve multiple banks, each taking a fee, making remittances expensive."},
            {"text": "Slow settlement times, often taking several business days.", "correct": True, "feedback": "Correct. Fintech solutions can offer near-instant settlement, compared to the slow pace of legacy systems."},
            {"text": "They can only be sent during normal business hours.", "correct": False, "feedback": "While settlement might be slow, the initiation can often be done 24/7 online. Fintech makes the whole process 24/7."},
            {"text": "They are not available for amounts less than $10,000.", "correct": False, "feedback": "Incorrect. Small remittances are very common, but they are often subject to disproportionately high fees."}
        ]
    },
    {
        "title": "Fintech: Account Aggregators",
        "description": "*Global Mini Highlight: India's Account Aggregator (AA) network has become a model for secure financial data sharing, with over 100 million users by 2025.*\n\nWhat are two functions of an Account Aggregator?",
        "category": "fintech",
        "references": "- **Framework:** [Account Aggregator India](https://sahamati.org.in/what-is-aa/)",
        "choices": [
            {"text": "To allow a user to securely share their financial data from one institution with another.", "correct": True, "feedback": "Correct. It acts as a 'consent manager' for data sharing, without seeing the data itself."},
            {"text": "To enable easier access to credit by providing a consolidated financial view to lenders.", "correct": True, "feedback": "Correct. Users can share their complete financial history, from multiple banks, to get better loan terms."},
            {"text": "To combine all the user's money into a single government-managed bank account.", "correct": False, "feedback": "Incorrect. It only manages the flow of data, not the actual funds."},
            {"text": "To provide investment advice and manage the user's stock portfolio.", "correct": False, "feedback": "Incorrect. An AA is a data-sharing utility, not a financial advisor."}
        ]
    },
    {
        "title": "Fintech: Web3 Identity",
        "description": "*Global Mini Highlight: In 2025, a 'login with your wallet' feature is as common as 'login with Google,' especially on e-commerce sites exploring token-gated commerce.*\n\nWhat are two principles of Web3 Identity?",
        "category": "fintech",
        "references": "- **Concept:** [Decentralized Identity](https://www.coinbase.com/learn/crypto-basics/what-is-decentralized-identity)",
        "choices": [
            {"text": "It is self-sovereign, meaning the user controls their own identity data.", "correct": True, "feedback": "Correct. Instead of relying on a company like Google, your identity is controlled from your personal crypto wallet."},
            {"text": "It uses the blockchain as a public key infrastructure to verify credentials.", "correct": True, "feedback": "Correct. Ownership of a wallet address can be cryptographically proven, forming the basis of identity verification."},
            {"text": "It requires you to submit your physical passport to a central database.", "correct": False, "feedback": "Incorrect. The goal is to move away from centralized databases and physical documents."},
            {"text": "It is controlled and issued by a single tech company.", "correct": False, "feedback": "Incorrect. This describes Web2 identity (e.g., Google, Facebook), which Web3 aims to replace."}
        ]
    },
    {
        "title": "Fintech: DeFi Insurance",
        "description": "*Global Mini Highlight: After several high-profile hacks, DeFi insurance protocols like Nexus Mutual covered over $500 million in user losses in 2024.*\n\nWhat are two features of DeFi insurance?",
        "category": "fintech",
        "references": "- **Service:** [DeFi Insurance](https://www.investopedia.com/what-is-decentralized-insurance-5217351)",
        "choices": [
            {"text": "It typically provides coverage against specific technical risks like smart contract failure.", "correct": True, "feedback": "Correct. This is a primary use case—insuring against bugs in the code of other DeFi protocols."},
            {"text": "It often operates as a mutual, where members share risk and contribute to a capital pool.", "correct": True, "feedback": "Correct. This peer-to-peer model is common, where the users are also the underwriters of the insurance."},
            {"text": "It is provided for free to all users of DeFi.", "correct": False, "feedback": "Incorrect. Users must pay a premium to purchase coverage, just like with traditional insurance."},
            {"text": "It is legally required for all cryptocurrency wallets.", "correct": False, "feedback": "Incorrect. DeFi insurance is an optional product that users can choose to buy."}
        ]
    },
    {
        "title": "Fintech: ESG Data & AI",
        "description": "*Global Mini Highlight: By 2025, AI-powered platforms are the primary tool for investors to analyze unstructured ESG data from company reports and news.*\n\nWhat are two ways AI helps with ESG investing?",
        "category": "fintech",
        "references": "- **Concept:** [ESG Investing](https.www.investopedia.com/terms/e/environmental-social-and-governance-esg-criteria.asp)",
        "choices": [
            {"text": "By using Natural Language Processing (NLP) to scan reports for greenwashing.", "correct": True, "feedback": "Correct. AI can analyze the language companies use to detect inconsistencies between their claims and actions."},
            {"text": "By aggregating and standardizing ESG data from thousands of different sources.", "correct": True, "feedback": "Correct. AI helps make sense of the vast and often inconsistent ESG data landscape."},
            {"text": "By guaranteeing that any company with a high ESG score will have a rising stock price.", "correct": False, "feedback": "Incorrect. ESG scores and stock performance are not perfectly correlated; AI is a tool for analysis, not a crystal ball."},
            {"text": "By investing in companies that have the most social media followers.", "correct": False, "feedback": "Incorrect. This is a poor metric for genuine ESG performance."}
        ]
    },

    # --- Finance & Stock Market Questions (20) ---
    {
        "title": "Stock Market: Market Capitalization",
        "description": "*Global Mini Highlight: Several Indian companies joined the $1 trillion market cap club in the 2024-2025 bull run.*\n\nWhich two statements about 'Market Cap' are correct?",
        "category": "general_finance",
        "references": "- **Metric:** [Market Capitalization](https://www.investopedia.com/terms/m/marketcapitalization.asp)",
        "choices": [
            {"text": "It is calculated by multiplying the share price by the number of outstanding shares.", "correct": True, "feedback": "This is the formula for calculating a company's market cap."},
            {"text": "It is used to categorize companies into sizes like 'small-cap', 'mid-cap', and 'large-cap'.", "correct": True, "feedback": "These categories are standard in the industry and are based directly on market cap levels."},
            {"text": "It represents the total amount of cash a company has.", "correct": False, "feedback": "Cash on hand is a different metric found on the balance sheet."},
            {"text": "A company can never have a market cap higher than its annual revenue.", "correct": False, "feedback": "Many growth companies have market caps that are many multiples of their revenue."}
        ]
    },
    {
        "title": "Stock Market: Bull and Bear Markets",
        "description": "*Global Mini Highlight: The global markets experienced a sharp bear market in early 2024, followed by a strong bull market recovery into 2025.*\n\nWhich two definitions are correct?",
        "category": "general_finance",
        "references": "- **Concept:** [Bull vs. Bear Market](https://www.investopedia.com/insights/digging-deeper-bull-and-bear-markets/)",
        "choices": [
            {"text": "A 'bull market' is a period of generally rising prices and investor optimism.", "correct": True, "feedback": "This correctly defines a bull market."},
            {"text": "A 'bear market' is often defined as a market decline of 20% or more from recent highs.", "correct": True, "feedback": "This 20% decline is the commonly accepted technical definition of a bear market."},
            {"text": "A 'bear market' is when trading volumes are at their highest.", "correct": False, "feedback": "Trading volumes can be high in both bull and bear markets, often spiking during periods of panic selling."},
            {"text": "A 'bull market' refers exclusively to the market for livestock.", "correct": False, "feedback": "While the terms originate from the way the animals attack, in finance they refer to market direction."}
        ]
    },
    {
        "title": "Stock Market: P/E Ratio",
        "description": "*Global Mini Highlight: The P/E ratio for the AI sector reached extreme highs in 2024 before correcting in 2025.*\n\nWhat are two valid interpretations of a high Price-to-Earnings (P/E) ratio?",
        "category": "general_finance",
        "references": "- **Metric:** [Price-to-Earnings (P/E) Ratio](https://www.investopedia.com/terms/p/price-earningsratio.asp)",
        "choices": [
            {"text": "The market has high expectations for the company's future earnings growth.", "correct": True, "feedback": "This is the primary reason investors pay a premium for a stock relative to its current earnings."},
            {"text": "The stock may be overvalued compared to its peers or its own historical average.", "correct": True, "feedback": "A high P/E ratio can also be a warning sign of an inflated stock price that is not justified by fundamentals."},
            {"text": "The company has very low or negative earnings.", "correct": False, "feedback": "If earnings are negative, the P/E ratio is typically not applicable (N/A)."},
            {"text": "The company operates in a slow-growth, stable industry like utilities.", "correct": False, "feedback": "Companies in such industries usually have low and stable P/E ratios."}
        ]
    },
    {
        "title": "Stock Market: ETF vs. Mutual Fund",
        "description": "*Global Mini Highlight: By 2025, total assets in ETFs globally have surpassed those in actively managed mutual funds.*\n\nWhich two statements correctly differentiate ETFs from Mutual Funds?",
        "category": "general_finance",
        "references": "- **Comparison:** [ETF vs. Mutual Fund](https://www.investopedia.com/articles/investing/032615/how-trade-etfs-vs-mutual-funds.asp)",
        "choices": [
            {"text": "ETFs can be bought and sold throughout the trading day at changing prices.", "correct": True, "feedback": "This intraday tradability is a key feature of ETFs, which are listed on stock exchanges."},
            {"text": "Mutual funds are priced only once per day, at the Net Asset Value (NAV) after markets close.", "correct": True, "feedback": "All buy and sell orders for a mutual fund placed during the day are executed at this single price."},
            {"text": "ETFs are always actively managed, while mutual funds are always passive.", "correct": False, "feedback": "Both fund types can be either actively managed or passively track an index."},
            {"text": "You can only buy mutual funds with cryptocurrency.", "correct": False, "feedback": "Both are purchased with traditional fiat currency."}
        ]
    },
    {
        "title": "Stock Market: Dividends",
        "description": "*Global Mini Highlight: In 2025, mature, cash-rich technology companies are increasingly initiating dividend payments to attract value investors.*\n\nWhich two are true statements about stock dividends?",
        "category": "general_finance",
        "references": "- **Concept:** [Dividend](https://www.investopedia.com/terms/d/dividend.asp)",
        "choices": [
            {"text": "They are a way for a company to distribute its profits to shareholders.", "correct": True, "feedback": "This is the definition of a dividend—a reward to the owners of the company."},
            {"text": "Companies are not legally obligated to pay dividends.", "correct": True, "feedback": "A company's board of directors decides whether to pay a dividend; it is not a requirement."},
            {"text": "The dividend payment causes the company's stock price to increase.", "correct": False, "feedback": "On the ex-dividend date, the stock price typically drops by about the dividend amount, as that cash is no longer part of the company's value."},
            {"text": "Only companies older than 50 years are allowed to pay dividends.", "correct": False, "feedback": "Incorrect. Companies of any age can pay dividends if they have the profits and choose to do so."}
        ]
    },
    {
        "title": "Stock Market: Short Selling",
        "description": "*Global Mini Highlight: The 'meme stock' craze of the early 2020s taught many new traders painful lessons about the risks of short selling.*\n\nWhat are two significant risks of short selling a stock?",
        "category": "general_finance",
        "references": "- **Strategy:** [Short Selling](https://www.investopedia.com/terms/s/shortselling.asp)",
        "choices": [
            {"text": "The potential for unlimited losses.", "correct": True, "feedback": "Since a stock's price can theoretically rise indefinitely, the potential loss for a short seller is unlimited."},
            {"text": "The risk of a 'short squeeze,' where a rising price forces sellers to buy back shares.", "correct": True, "feedback": "A short squeeze can cause rapid and massive losses as short sellers are forced to close their positions at high prices."},
            {"text": "The risk that the company will pay a surprise dividend.", "correct": False, "feedback": "While a short seller has to pay the dividend, this is a known cost, not the primary risk compared to unlimited losses."},
            {"text": "The risk of the stock being delisted from the exchange.", "correct": False, "feedback": "A delisting would typically cause the stock price to plummet, which would be a profitable event for a short seller."}
        ]
    },
    {
        "title": "Stock Market: Blue-Chip vs. Penny Stock",
        "description": "*Global Mini Highlight: The market volatility of 2024 has led many new investors in 2025 to prefer the stability of blue-chip stocks.*\n\nWhich two descriptions apply to 'blue-chip' stocks?",
        "category": "general_finance",
        "references": "- **Concept:** [Blue-Chip Stock](https://www.investopedia.com/terms/b/bluechipstock.asp)",
        "choices": [
            {"text": "They are large, financially sound companies with a history of reliability.", "correct": True, "feedback": "This is the definition of a blue-chip stock (e.g., Reliance, HDFC Bank, TCS)."},
            {"text": "They often pay regular dividends to shareholders.", "correct": True, "feedback": "Their stable cash flows allow many blue-chip companies to pay consistent dividends."},
            {"text": "They are highly speculative and have a high risk of failure.", "correct": False, "feedback": "This describes penny stocks, not blue-chip stocks."},
            {"text": "They trade for very low prices, often less than ₹10 per share.", "correct": False, "feedback": "This is the definition of a penny stock."}
        ]
    },
    {
        "title": "Stock Market: Market Order vs. Limit Order",
        "description": "*Global Mini Highlight: High-frequency trading firms in 2025 exploit the tiny differences between market orders and the bid-ask spread to make profits.*\n\nWhich two statements accurately describe order types?",
        "category": "general_finance",
        "references": "- **Comparison:** [Order Types](https://www.investopedia.com/ask/answers/100314/whats-difference-between-market-order-and-limit-order.asp)",
        "choices": [
            {"text": "A 'market order' prioritizes speed of execution over a specific price.", "correct": True, "feedback": "A market order will execute immediately at the best available current price."},
            {"text": "A 'limit order' allows you to set a maximum price for a buy or a minimum price for a sell.", "correct": True, "feedback": "A limit order gives you control over the price but does not guarantee execution."},
            {"text": "A 'market order' guarantees you will get the last-traded price.", "correct": False, "feedback": "It guarantees execution at the *next available* price, which may be different from the last-traded price due to the bid-ask spread."},
            {"text": "A 'limit order' is guaranteed to execute within 24 hours.", "correct": False, "feedback": "A limit order will only execute if the market price reaches your specified limit, which may never happen."}
        ]
    },
    {
        "title": "General Finance: Diversification",
        "description": "*Global Mini Highlight: The synchronized global market downturn of 2024 showed the limits of simple stock diversification, leading investors in 2025 to seek broader asset class diversification.*\n\nWhich two are examples of diversification?",
        "category": "general_finance",
        "references": "- **Strategy:** [Diversification](https://www.investopedia.com/terms/d/diversification.asp)",
        "choices": [
            {"text": "Owning stocks from different industries (e.g., tech, healthcare, energy).", "correct": True, "feedback": "This is sector diversification, reducing the risk of a downturn in any single industry."},
            {"text": "Holding a mix of different asset classes (e.g., stocks, bonds, real estate).", "correct": True, "feedback": "This is asset class diversification, the broadest form of risk management."},
            {"text": "Putting all your money into the single best-performing stock of the last year.", "correct": False, "feedback": "This is concentration, the opposite of diversification."},
            {"text": "Buying shares of five different technology companies.", "correct": False, "feedback": "While this is a start, it is not broad diversification as you are still concentrated in a single industry."}
        ]
    },
    {
        "title": "General Finance: Compound Interest",
        "description": "*Global Mini Highlight: With savings rates higher in 2025 than in the previous decade, understanding compound interest has become crucial for wealth building.*\n\nWhat two factors have the greatest impact on its power?",
        "category": "general_finance",
        "references": "- **Concept:** [Compound Interest](https://www.investopedia.com/terms/c/compoundinterest.asp)",
        "choices": [
            {"text": "The amount of time the money is invested.", "correct": True, "feedback": "Time is the most critical ingredient, as it allows the 'interest on interest' effect to accelerate."},
            {"text": "The rate of return (interest rate).", "correct": True, "feedback": "A higher rate of return means your investment compounds more quickly."},
            {"text": "The name of the bank where the money is held.", "correct": False, "feedback": "The name of the institution is irrelevant to the mathematical principle of compounding."},
            {"text": "The day of the week you make your initial investment.", "correct": False, "feedback": "The starting day has a negligible effect over the long term."}
        ]
    },
    {
        "title": "General Finance: Credit Score",
        "description": "*Global Mini Highlight: As of 2025, fintech data (like timely bill payments) is increasingly being integrated into official CIBIL credit scores in India.*\n\nWhich two actions are most likely to improve your credit score?",
        "category": "general_finance",
        "references": "- **Metric:** [Credit Score](https://www.investopedia.com/terms/c/credit_score.asp)",
        "choices": [
            {"text": "Making all of your loan and credit card payments on time.", "correct": True, "feedback": "Payment history is the single most important factor in a credit score."},
            {"text": "Keeping your credit card balances low relative to their limits.", "correct": True, "feedback": "This is known as your credit utilization ratio, and keeping it low is very important."},
            {"text": "Closing all of your old credit card accounts.", "correct": False, "feedback": "This can actually hurt your score by reducing your average age of accounts and increasing your utilization ratio."},
            {"text": "Checking your credit score every single day.", "correct": False, "feedback": "Checking your own score (a 'soft inquiry') does not affect it, but it also doesn't improve it."}
        ]
    },
    {
        "title": "General Finance: Inflation",
        "description": "*Global Mini Highlight: After peaking in the early 2020s, inflation has remained stubbornly above central bank targets into 2025.*\n\nWhich two asset classes have historically performed well during high inflation?",
        "category": "general_finance",
        "references": "- **Concept:** [Inflation](https://www.investopedia.com/terms/i/inflation.asp)",
        "choices": [
            {"text": "Commodities, such as oil and metals.", "correct": True, "feedback": "The price of raw materials often rises with inflation, making them a good hedge."},
            {"text": "Real estate, as property values and rents tend to rise with prices.", "correct": True, "feedback": "Real estate is a physical asset that can provide protection against the declining value of currency."},
            {"text": "Long-term government bonds.", "correct": False, "feedback": "Inflation is very bad for long-term bonds, as it erodes the value of their fixed interest payments."},
            {"text": "Cash held in a savings account.", "correct": False, "feedback": "Inflation directly reduces the purchasing power of cash, making it a poor performer."}
        ]
    },
    {
        "title": "General Finance: Stocks vs. Bonds",
        "description": "*Global Mini Highlight: With interest rates high in 2025, bonds have become a more competitive alternative to stocks for the first time in over a decade.*\n\nIn the event of a company's bankruptcy, which two statements are true?",
        "category": "general_finance",
        "references": "- **Comparison:** [Stocks vs. Bonds](https://www.investopedia.com/articles/investing/050213/stocks-vs-bonds-which-should-you-buy.asp)",
        "choices": [
            {"text": "Bondholders are paid before stockholders.", "correct": True, "feedback": "As lenders, bondholders have a higher claim on the company's assets than owners (stockholders)."},
            {"text": "Stockholders are likely to lose their entire investment.", "correct": True, "feedback": "As residual claimants, stockholders are last in line and often receive nothing after the company's debts are paid."},
            {"text": "Stockholders and bondholders are paid out equally.", "correct": False, "feedback": "There is a strict hierarchy of repayment, and stockholders are at the bottom."},
            {"text": "The government is required to bail out all stockholders.", "correct": False, "feedback": "There is no government guarantee for stock investments."}
        ]
    },
    {
        "title": "General Finance: Net Worth",
        "description": "*Global Mini Highlight: A 2025 study shows that the median net worth for millennials has finally surpassed that of previous generations at the same age.*\n\nWhich two items are considered liabilities when calculating net worth?",
        "category": "general_finance",
        "references": "- **Metric:** [Net Worth](https://www.investopedia.com/terms/n/networth.asp)",
        "choices": [
            {"text": "The outstanding balance on your mortgage.", "correct": True, "feedback": "A mortgage is a debt, which is a liability."},
            {"text": "The amount you owe on your student loans.", "correct": True, "feedback": "Student loans are a form of debt and therefore a liability."},
            {"text": "The value of your car.", "correct": False, "feedback": "The car itself is an asset. The car loan would be the liability."},
            {"text": "The amount of money in your retirement account.", "correct": False, "feedback": "Your retirement account is a key asset."}
        ]
    },
    {
        "title": "General Finance: Emergency Fund",
        "description": "*Global Mini Highlight: The economic uncertainty of the early 2020s led to a permanent shift by 2025, with more households maintaining a larger emergency fund.*\n\nWhich two are key characteristics of a proper emergency fund?",
        "category": "general_finance",
        "references": "- **Concept:** [Emergency Fund](https://www.investopedia.com/terms/e/emergency_fund.asp)",
        "choices": [
            {"text": "It should be liquid, meaning easily accessible as cash.", "correct": True, "feedback": "The money needs to be available immediately, so a high-yield savings account is a common choice."},
            {"text": "It should typically cover 3-6 months of essential living expenses.", "correct": True, "feedback": "This is the standard financial planning advice to provide a cushion in case of job loss or other emergencies."},
            {"text": "It should be invested in high-growth technology stocks.", "correct": False, "feedback": "This would expose your emergency savings to market risk, defeating its purpose as a safety net."},
            {"text": "It should be used for planned expenses like vacations.", "correct": False, "feedback": "An emergency fund is strictly for unplanned, urgent financial needs."}
        ]
    },
    {
        "title": "General Finance: Capital Gains Tax",
        "description": "*Global Mini Highlight: Indian budget discussions in 2025 are focused on potentially equalizing the tax treatment of long-term and short-term capital gains.*\n\nWhich two statements are generally true about Capital Gains Tax?",
        "category": "general_finance",
        "references": "- **Concept:** [Capital Gains Tax](https://www.investopedia.com/terms/c/capital_gains_tax.asp)",
        "choices": [
            {"text": "It is a tax on the profit you make from selling an asset, like a stock or property.", "correct": True, "feedback": "This is the definition of a capital gain—the difference between the selling price and purchase price."},
            {"text": "Long-term capital gains are often taxed at a lower rate than short-term gains.", "correct": True, "feedback": "This is a common feature of tax codes (including India's) to incentivize long-term investment."},
            {"text": "You have to pay it every year you hold an asset, even if you don't sell it.", "correct": False, "feedback": "The tax is only 'realized' and due when you sell the asset for a profit."},
            {"text": "If you sell a stock for a loss, you receive a capital gains tax credit.", "correct": False, "feedback": "You realize a capital loss, which can be used to offset gains, but it's not a direct credit."}
        ]
    },
    {
        "title": "Stock Market: Fundamental vs. Technical Analysis",
        "description": "*Global Mini Highlight: The rise of AI trading in 2025 has led to new forms of hybrid analysis, combining technical and fundamental signals.*\n\nWhich two statements correctly describe these methods?",
        "category": "general_finance",
        "references": "- **Comparison:** [Fundamental vs. Technical Analysis](https://www.investopedia.com/articles/investing/052813/fundamental-vs-technical-analysis.asp)",
        "choices": [
            {"text": "Fundamental analysis involves examining a company's financial health and statements.", "correct": True, "feedback": "It focuses on metrics like revenue, earnings, and debt to determine a company's intrinsic value."},
            {"text": "Technical analysis involves studying price charts and trading volumes to identify patterns.", "correct": True, "feedback": "It focuses on market psychology and past price movements to predict future trends."},
            {"text": "Fundamental analysis is only useful for short-term day trading.", "correct": False, "feedback": "It is primarily used for long-term investing."},
            {"text": "Technical analysis determines the exact price a stock 'should' be worth.", "correct": False, "feedback": "It attempts to predict price direction, not calculate intrinsic value."}
        ]
    },
    {
        "title": "Stock Market: Economic Moat",
        "description": "*Global Mini Highlight: Warren Buffett's 2025 shareholder letter reiterated his focus on investing in companies with durable 'economic moats'.*\n\nWhat are two examples of a company's economic moat?",
        "category": "general_finance",
        "references": "- **Concept:** [Economic Moat](https://www.investopedia.com/terms/e/economicmoat.asp)",
        "choices": [
            {"text": "Strong brand recognition, like Apple or Coca-Cola.", "correct": True, "feedback": "A powerful brand allows a company to charge premium prices and maintain customer loyalty."},
            {"text": "High switching costs, where it is difficult for customers to move to a competitor.", "correct": True, "feedback": "For example, a business is unlikely to switch its entire operating system from Windows to something else."},
            {"text": "Having the most employees in the industry.", "correct": False, "feedback": "A large number of employees is a cost, not necessarily a competitive advantage."},
            {"text": "Having a very high stock price.", "correct": False, "feedback": "A high stock price is the result of market perception, not an underlying competitive advantage."}
        ]
    },
    {
        "title": "Stock Market: Hedging",
        "description": "*Global Mini Highlight: Due to increased market volatility in 2025, the use of hedging instruments by retail investors has seen a significant rise.*\n\nWhat are two common ways an investor might 'hedge' a stock portfolio?",
        "category": "general_finance",
        "references": "- **Strategy:** [Hedging](https://www.investopedia.com/terms/h/hedge.asp)",
        "choices": [
            {"text": "Buying put options on a market index like the S&P 500.", "correct": True, "feedback": "If the market falls, the value of the put options will rise, offsetting some of the losses in the stock portfolio."},
            {"text": "Short-selling an index ETF that tracks the overall market.", "correct": True, "feedback": "This creates a position that profits from a market decline, counteracting losses in their long stock positions."},
            {"text": "Selling all their stocks and holding only cash.", "correct": False, "feedback": "This is exiting the market, not hedging. Hedging is about reducing risk while maintaining a position."},
            {"text": "Doubling down and buying more of the stocks they already own.", "correct": False, "feedback": "This increases risk and concentration, which is the opposite of hedging."}
        ]
    },
    {
        "title": "Stock Market: Calls vs. Puts",
        "description": "*Global Mini Highlight: Options trading volume hit an all-time high in 2025 as investors used them for both speculation and hedging.*\n\nWhich two statements about options trading are correct?",
        "category": "general_finance",
        "references": "- **Comparison:** [Call vs. Put](https://www.investopedia.com/ask/answers/04/033104.asp)",
        "choices": [
            {"text": "Buying a 'call option' gives you the right, but not the obligation, to buy a stock at a set price.", "correct": True, "feedback": "This is the definition of a call option. It's a bullish bet that the stock price will rise."},
            {"text": "Buying a 'put option' gives you the right, but not the obligation, to sell a stock at a set price.", "correct": True, "feedback": "This is the definition of a put option. It's a bearish bet that the stock price will fall."},
            {"text": "A 'call option' is a bet that the stock price will go down.", "correct": False, "feedback": "This is incorrect; a call option is a bet on the price going up."},
            {"text": "You are legally required to exercise any option you buy.", "correct": False, "feedback": "Options give you the 'right, not the obligation.' Many options expire worthless if they are not profitable to exercise."}
        ]
    },
    {
        "title": "General Finance: Alternative Investments",
        "description": "*Global Mini Highlight: With public market returns becoming more correlated in 2025, institutional investors are increasing their allocation to alternative investments.*\n\nWhich two are examples of 'alternative investments'?",
        "category": "general_finance",
        "references": "- **Asset Class:** [Alternative Investment](https://www.investopedia.com/terms/a/alternative_investment.asp)",
        "choices": [
            {"text": "Private Equity, which involves investing in privately-held companies.", "correct": True, "feedback": "Correct. This is a classic alternative investment, not accessible on public stock exchanges."},
            {"text": "Venture Capital, which focuses on funding early-stage startup companies.", "correct": True, "feedback": "Correct. This is a high-risk, high-return subset of private equity."},
            {"text": "A publicly-traded blue-chip stock like Reliance Industries.", "correct": False, "feedback": "Incorrect. This is a traditional investment, not an alternative one."},
            {"text": "A government savings bond.", "correct": False, "feedback": "Incorrect. Government bonds are a core traditional asset class."}
        ]
    },
    # --- General Knowledge (GK) Questions (10) ---
    {
        "title": "GK: Global Supply Chains",
        "description": "*Global Mini Highlight: After the supply chain disruptions of the early 2020s, many multinational corporations have shifted to a 'China Plus One' strategy.*\n\nWhat are two primary goals of this strategy?",
        "category": "gk",
        "references": "- **Strategy:** [China Plus One](https://www.investopedia.com/terms/c/china-plus-one-strategy.asp)",
        "choices": [
            {"text": "To reduce dependency on manufacturing in a single country.", "correct": True, "feedback": "Correct. The main goal is to diversify the supply chain to avoid being reliant on only China."},
            {"text": "To mitigate geopolitical and trade-related risks.", "correct": True, "feedback": "Correct. By having operations in other countries (e.g., Vietnam, India, Mexico), companies are less vulnerable to trade disputes involving China."},
            {"text": "To exclusively use Chinese suppliers for all materials.", "correct": False, "feedback": "Incorrect. This strategy is about diversifying *away* from an exclusive reliance on China."},
            {"text": "To move all manufacturing operations back to the company's home country.", "correct": False, "feedback": "Incorrect. That describes 'reshoring'; 'China Plus One' involves adding another foreign location, not necessarily returning home."}
        ]
    },
    {
        "title": "GK: The Green Energy Transition",
        "description": "*Global Mini Highlight: The 2025 Global Climate Accord has accelerated investment in renewable energy, impacting commodity markets.*\n\nWhat are two commodities that have seen increased demand due to this transition?",
        "category": "gk",
        "references": "- **Topic:** [Green Energy Commodities](https://www.ig.com/en/trading-strategies/what-are-green-commodities-and-how-do-you-trade-them--220721)",
        "choices": [
            {"text": "Lithium, a key component in electric vehicle (EV) batteries.", "correct": True, "feedback": "Correct. The explosion in EV production has led to a massive demand surge for lithium."},
            {"text": "Copper, which is used extensively in wiring for EVs and renewable energy infrastructure.", "correct": True, "feedback": "Correct. Electrification requires vast amounts of copper, making it a critical 'green' commodity."},
            {"text": "Coal, used to power traditional energy grids.", "correct": False, "feedback": "Incorrect. The green energy transition is focused on moving *away* from fossil fuels like coal."},
            {"text": "Natural Gas, often used as a 'bridge fuel'.", "correct": False, "feedback": "While used, the primary demand increase is for the metals enabling electrification, not another fossil fuel."}
        ]
    },
    {
        "title": "GK: Semiconductor Manufacturing",
        "description": "*Global Mini Highlight: By 2025, geopolitical tensions have made semiconductor supply chain security a top priority for nations like the US, India, and Japan.*\n\nWhat are two major hubs for advanced semiconductor manufacturing?",
        "category": "gk",
        "references": "- **Industry:** [Semiconductors](https://www.investopedia.com/terms/s/semiconductor.asp)",
        "choices": [
            {"text": "Taiwan, home to industry giant TSMC.", "correct": True, "feedback": "Correct. Taiwan is the world's leader in the manufacturing of the most advanced logic chips."},
            {"text": "South Korea, home to major players like Samsung.", "correct": True, "feedback": "Correct. South Korea is a powerhouse in both memory chips and advanced semiconductor fabrication."},
            {"text": "Brazil, known for its commodity exports.", "correct": False, "feedback": "Incorrect. Brazil is a major player in agriculture and commodities, not advanced semiconductors."},
            {"text": "Russia, a major exporter of oil and gas.", "correct": False, "feedback": "Incorrect. Russia's economy is focused on energy exports, not high-tech chip manufacturing."}
        ]
    },
    {
        "title": "GK: Demographics and Economies",
        "description": "*Global Mini Highlight: A 2025 UN report highlights the 'demographic dividend' in countries like India, contrasting with the aging populations in Japan and Italy.*\n\nWhat are two economic implications of a country having a young population?",
        "category": "gk",
        "references": "- **Concept:** [Demographic Dividend](https://www.investopedia.com/terms/d/demographic-dividend.asp)",
        "choices": [
            {"text": "A potentially larger and more dynamic workforce.", "correct": True, "feedback": "Correct. A larger working-age population can drive economic growth and productivity."},
            {"text": "A growing consumer market, which can attract foreign investment.", "correct": True, "feedback": "Correct. More young people means more consumers buying goods and services, making the market attractive."},
            {"text": "A higher tax burden to support a large number of retirees.", "correct": False, "feedback": "Incorrect. This is a challenge for countries with aging populations, not young ones."},
            {"text": "A shrinking economy due to lack of experienced workers.", "correct": False, "feedback": "Incorrect. A young population is generally seen as a major catalyst for economic expansion."}
        ]
    },
    {
        "title": "GK: Remote Work's Economic Impact",
        "description": "*Global Mini Highlight: In 2025, major tech companies are reducing their office footprints in expensive cities like San Francisco and Bengaluru.*\n\nWhat are two economic effects of the widespread adoption of remote work?",
        "category": "gk",
        "references": "- **Trend:** [Remote Work Economics](https://www.forbes.com/advisor/business/remote-work-statistics/)",
        "choices": [
            {"text": "Downward pressure on commercial real estate prices in major city centers.", "correct": True, "feedback": "Correct. If companies need less office space, the demand for it decreases, leading to lower rents and values."},
            {"text": "A potential economic boost for smaller, 'Tier 2' cities and suburban areas.", "correct": True, "feedback": "Correct. If people can work from anywhere, they may move to areas with a lower cost of living, bringing their salaries with them."},
            {"text": "An increase in daily commuting traffic into city centers.", "correct": False, "feedback": "Incorrect. Remote work significantly reduces the number of daily commuters."},
            {"text": "A mandatory requirement for all employees to live within 5 km of their office.", "correct": False, "feedback": "Incorrect. Remote work allows employees to live much farther away from their company's physical office."}
        ]
    },
    {
        "title": "GK: Carbon Credit Markets",
        "description": "*Global Mini Highlight: The price of carbon credits on the EU's Emissions Trading System (ETS) has become a key indicator for industrial companies in 2025.*\n\nWhat are two functions of a carbon credit?",
        "category": "gk",
        "references": "- **Concept:** [Carbon Credit](https://www.investopedia.com/terms/c/carbon_credit.asp)",
        "choices": [
            {"text": "It represents a permit allowing a company to emit one ton of carbon dioxide.", "correct": True, "feedback": "Correct. It's a tradable permit scheme to cap total emissions."},
            {"text": "It creates a financial incentive for companies to reduce their emissions.", "correct": True, "feedback": "Correct. If a company emits less, it can sell its unused credits for a profit."},
            {"text": "It is a consumer product that individuals can burn for heat.", "correct": False, "feedback": "Incorrect. It is a financial instrument, not a physical fuel."},
            {"text": "It provides a tax deduction for driving a gasoline-powered car.", "correct": False, "feedback": "Incorrect. It is a market mechanism for corporations, not a personal tax deduction."}
        ]
    },
    {
        "title": "GK: Economics of Space Exploration",
        "description": "*Global Mini Highlight: By 2025, private companies like SpaceX and Blue Origin have made access to low Earth orbit significantly cheaper.*\n\nWhat are two major economic opportunities created by this?",
        "category": "gk",
        "references": "- **Industry:** [Space Economy](https://www.morganstanley.com/ideas/investing-in-space)",
        "choices": [
            {"text": "The deployment of large satellite constellations for global internet access.", "correct": True, "feedback": "Correct. Lower launch costs make projects like Starlink economically viable."},
            {"text": "New possibilities for in-space manufacturing and asteroid mining.", "correct": True, "feedback": "Correct. While still early, cheaper access is the first step toward making these futuristic industries possible."},
            {"text": "A decrease in the value of all technology stocks on Earth.", "correct": False, "feedback": "Incorrect. The space economy is an extension of the tech sector and is seen as a major growth area."},
            {"text": "A global agreement to stop all future space launches.", "correct": False, "feedback": "Incorrect. The trend is toward a rapid increase in space activity, not a decrease."}
        ]
    },
    {
        "title": "GK: AI's Impact on Labor Markets",
        "description": "*Global Mini Highlight: A 2025 study showed that AI has automated 15% of routine analytical jobs but created new roles in AI management and data science.*\n\nWhat are two recognized impacts of AI on the labor market?",
        "category": "gk",
        "references": "- **Trend:** [AI and the Future of Jobs](https://www.weforum.org/reports/the-future-of-jobs-report-2023/)",
        "choices": [
            {"text": "It can automate repetitive tasks, increasing productivity in some roles.", "correct": True, "feedback": "Correct. AI is excellent at handling routine data processing and analysis, freeing up humans for more complex tasks."},
            {"text": "It creates new job categories that did not exist before, like 'prompt engineer' or 'AI ethicist'.", "correct": True, "feedback": "Correct. As with past technological shifts, AI eliminates some jobs while creating entirely new ones."},
            {"text": "It has resulted in a permanent increase in the global unemployment rate.", "correct": False, "feedback": "Incorrect. Historically, technology has displaced jobs but has not led to a permanent rise in overall unemployment due to the creation of new roles."},
            {"text": "It has made all forms of human labor completely obsolete.", "correct": False, "feedback": "Incorrect. AI is a tool that complements human labor; tasks requiring creativity, empathy, and complex problem-solving remain in high demand."}
        ]
    },
    {
        "title": "GK: Water Scarcity as an Economic Risk",
        "description": "*Global Mini Highlight: In 2025, cities like Cape Town and Chennai are implementing permanent water rationing, impacting local industries.*\n\nWhat are two economic consequences of severe water scarcity?",
        "category": "gk",
        "references": "- **Risk:** [Water Scarcity](https://www.worldbank.org/en/topic/water/overview)",
        "choices": [
            {"text": "Disruption to agriculture, leading to lower crop yields and higher food prices.", "correct": True, "feedback": "Correct. Agriculture is the largest consumer of fresh water, and scarcity directly impacts food production."},
            {"text": "Increased operational costs and risks for industries like manufacturing and energy production.", "correct": True, "feedback": "Correct. Many industrial processes, from making semiconductors to cooling power plants, require vast amounts of water."},
            {"text": "A global decrease in the price of bottled water.", "correct": False, "feedback": "Incorrect. Scarcity of a resource typically leads to an increase in the price of its substitutes."},
            {"text": "An increase in the population of all major deserts.", "correct": False, "feedback": "Incorrect. This describes desertification, which is a cause of water scarcity, not an economic consequence of it."}
        ]
    },
    {
        "title": "GK: Rare Earth Metals",
        "description": "*Global Mini Highlight: Geopolitical tensions in 2025 have led to fears of a supply disruption for rare earth metals, critical for the tech and defense industries.*\n\nWhich two are true statements about rare earth metals?",
        "category": "gk",
        "references": "- **Resource:** [Rare Earth Metals](https://www.investopedia.com/terms/r/rare-earth-element.asp)",
        "choices": [
            {"text": "They are essential components in many modern technologies, including smartphones and EVs.", "correct": True, "feedback": "Correct. Their unique magnetic and electronic properties are vital for high-tech manufacturing."},
            {"text": "China is the dominant global producer, creating supply chain risks for other countries.", "correct": True, "feedback": "Correct. China's control over the mining and processing of rare earths is a significant geopolitical factor."},
            {"text": "They are called 'rare' because they are less abundant in the Earth's crust than gold.", "correct": False, "feedback": "Incorrect. They are relatively abundant, but are difficult and environmentally damaging to mine and process."},
            {"text": "They are primarily used to make stainless steel.", "correct": False, "feedback": "Incorrect. The primary components of stainless steel are iron, chromium, and nickel."}
        ]
    }
]
