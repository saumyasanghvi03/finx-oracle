SCENARIOS = [
    {
        "title": "The Crypto Exchange Heist",
        "description": "Your AI-driven fraud detection system, **finAIguard**, flags an anomaly. A long-standing, high-net-worth client with a history of steady, large-sum transactions suddenly initiates a series of 50 small, identical transfers to 50 different, previously unknown recipients in various jurisdictions over a span of 30 minutes. The total value is significant.",
        "choices": [
            {"text": "A. Immediately decline all transfers and freeze the client's account, citing a high-risk security alert.", "correct": False, "feedback": "An immediate freeze is too aggressive for an established client and could lead to a customer service crisis. Behavioral analysis is a better first step."},
            {"text": "B. Automatically approve the first transfer to avoid service disruption and flag the remaining 49 for manual review.", "correct": False, "feedback": "This is a poor security practice; it allows the initial portion of a potentially fraudulent transaction to go through."},
            {"text": "C. Soft-flag the account and trigger an internal review, while simultaneously implementing a **behavioral analytics model** to compare this new pattern against the client's historical data for real-time risk scoring.", "correct": True, "feedback": "Correct. This is a balanced, AI-driven approach. It avoids a public-facing service disruption while using advanced analytics to determine the true risk."}
        ],
        "project_link": "https://github.com/saumyasanghvi03/finAIguard"
    },
    {
        "title": "The FinTech Startup's Flaw",
        "description": "A new fintech startup integrates a real-time payment gateway. They are experiencing a high volume of transactions, and their initial rule-based fraud engine is generating a massive number of false positives, frustrating legitimate users. They need a more effective solution.",
        "choices": [
            {"text": "A. Implement a static **deep learning model** trained on historical fraud data, which is faster and more accurate than their current rule-based system.", "correct": False, "feedback": "While effective, a static model will struggle to adapt to new fraud patterns over time."},
            {"text": "B. Utilize a **hybrid model** that combines the initial rules-based system with an AI layer that focuses on detecting zero-day fraud patterns and reducing false positives through anomaly detection.", "correct": True, "feedback": "Correct. A hybrid model is the optimal solution. It leverages the speed of existing rules while using AI for continuous learning and precision, a key feature of **finAIguard**."},
            {"text": "C. Replace their existing system with a pure **neural network** model that requires no pre-set rules, making it entirely autonomous.", "correct": False, "feedback": "A pure neural network can be brittle and prone to errors if not consistently trained on a wide range of data, potentially causing even more false positives."}
        ],
        "project_link": "https://github.com/saumyasanghvi03/finAIguard"
    },
    {
        "title": "The On-Chain Laundering Scheme",
        "description": "You are a compliance officer at a major cryptocurrency exchange. Your **onchain-aml-dashboard** identifies a user who has just deposited a large amount of a popular stablecoin. The funds originated from a complex series of transactions involving a privacy-enhancing mixer service, a series of low-value dust attacks on other wallets, and a final consolidation through a decentralized exchange (DEX).",
        "choices": [
            {"text": "A. Immediately file a Suspicious Activity Report (SAR) with the relevant financial authorities, as this activity is a clear indication of money laundering.", "correct": False, "feedback": "While suspicious, you need more data. An immediate SAR without an internal investigation can be premature and damage a user's reputation."},
            {"text": "B. Initiate an enhanced due diligence (EDD) review of the user, while flagging the transaction for further analysis to determine if the pattern is part of a larger, illicit network.", "correct": True, "feedback": "Correct. This is the standard procedure. The pattern of mixers, dust attacks, and DEX swaps is highly indicative of layering, a stage in money laundering. This action aligns with the purpose of an **onchain-aml-dashboard**."},
            {"text": "C. Approve the transaction without a red flag, as the funds are now in a stablecoin, which is generally considered a lower-risk asset.", "correct": False, "feedback": "Incorrect. The asset type doesn't absolve the transaction's history. The source of funds is the key factor, not the final asset."}
        ],
        "project_link": "https://github.com/saumyasanghvi03/onchain-aml-dashboard"
    },
    {
        "title": "The DeFi Protocol Audit",
        "description": "A decentralized finance (DeFi) protocol wants to ensure it is not being used for illicit activities. They need a way to monitor transactions without compromising the privacy of their users.",
        "choices": [
            {"text": "A. **Token-specific risk scoring** that assigns a risk rating to a user's wallet based on its interaction with high-risk tokens.", "correct": False, "feedback": "This is a useful feature but doesn't address the core problem of identifying complex, multi-wallet schemes."},
            {"text": "B. A **zero-knowledge proof (ZKP)**-based system that verifies the legitimacy of a user's funds without revealing their transaction history.", "correct": False, "feedback": "While a ZKP system can be used for compliance, its primary use is for privacy, not for identifying illicit fund flows after the fact."},
            {"text": "C. An **address clustering** tool that groups wallets based on their transactional behavior to identify patterns of layering and fund commingling.", "correct": True, "feedback": "Correct. **Address clustering** is the key feature of a professional on-chain AML dashboard. It helps link seemingly unrelated wallets to a single user or group, uncovering large-scale money laundering networks."}
        ],
        "project_link": "https://github.com/saumyasanghvi03/onchain-aml-dashboard"
    },
    {
        "title": "The Derivatives Dilemma",
        "description": "A portfolio manager holds a significant position in a volatile tech stock. They are concerned about a potential short-term price drop but do not want to sell their shares. They are looking for a way to mitigate this downside risk while still retaining ownership.",
        "choices": [
            {"text": "A. Execute a **futures contract** to sell the stock at a future date, effectively locking in the current price.", "correct": False, "feedback": "A futures contract is a binding agreement to sell, which would force them to sell their shares."},
            {"text": "B. Purchase a **put option**, which gives them the right, but not the obligation, to sell the stock at a pre-determined price if the market falls.", "correct": True, "feedback": "Correct. A **put option** is the classic hedging strategy for a long position, as it provides protection against a price drop without forcing a sale."},
            {"text": "C. Initiate a **covered call strategy**, which involves selling a call option to generate income from the stock's potential upside.", "correct": False, "feedback": "A covered call is an income-generating strategy, but it does not protect against downside risk; it limits the upside and provides little downside protection."}
        ],
        "project_link": "https://github.com/saumyasanghvi03/DerivX"
    },
    {
        "title": "The Quant's Leverage",
        "description": "A quantitative trader believes a stock is undervalued but needs to leverage a small amount of capital to maximize potential gains. They want to bet on a significant price increase in the next month, with limited downside risk if they are wrong.",
        "choices": [
            {"text": "A. It would provide the probability of the stock reaching a certain price, helping them decide which strike price to choose for a **call option**.", "correct": True, "feedback": "Correct. The **blockscholes** model is foundational for pricing options. By analyzing the variables, it helps a trader choose the optimal strike price to maximize leverage."},
            {"text": "B. It would calculate the fair value of a **put option**, allowing them to determine if it is overpriced for an arbitrage opportunity.", "correct": False, "feedback": "While the model can do this, it doesn't align with the trader's goal of leveraging a bullish bet."},
            {"text": "C. It would generate a real-time volatility index for the stock, allowing them to time their entry and exit points precisely.", "correct": False, "feedback": "The model uses volatility as an input, but generating a real-time volatility index is a different function."}
        ],
        "project_link": "https://github.com/saumyasanghvi03/blockscholes"
    },
    {
        "title": "The On-Chain Sleuth",
        "description": "A major cryptocurrency exchange reports that a wallet address has been compromised, resulting in a large theft of funds. The hacker immediately moved the stolen assets across multiple chains. You are a blockchain investigator.",
        "choices": [
            {"text": "A. Search for the hacker's IP address to pinpoint their geographic location for law enforcement.", "correct": False, "feedback": "Blockchain is pseudonymous and does not store IP addresses. This is not a valid on-chain investigation step."},
            {"text": "B. Paste the compromised wallet's address into the terminal and trace the initial outflow of funds to identify the first recipient's address.", "correct": True, "feedback": "Correct. This is the first and most critical step in an on-chain investigation. A **BlockVista Terminal** provides a direct way to follow the money trail."},
            {"text": "C. Analyze the transaction history of a known 'whale' wallet to see if they are somehow connected to the hack.", "correct": False, "feedback": "This is a speculative step and a poor starting point. The investigation must begin with the known compromised address."}
        ],
        "project_link": "https://github.com/saumyasanghvi03/BlockVista-Terminal"
    },
    {
        "title": "The Smart Contract Verification",
        "description": "A developer has deployed a new smart contract for a token launch. They need to verify that the contract's code is correct and that it has been deployed to the correct network address.",
        "choices": [
            {"text": "A. By running the contract's code in a local simulated environment to check for bugs.", "correct": False, "feedback": "This is a good practice for development, but it doesn't verify the code that is *actually* on the blockchain."},
            {"text": "B. By displaying the contract's source code, allowing the developer to verify it against the bytecode on the blockchain.", "correct": True, "feedback": "Correct. A key feature of a **blockchain explorer** is the ability to verify that the deployed contract code matches the source code, ensuring trust and transparency."},
            {"text": "C. By showing real-time market data to ensure the token's initial liquidity is sufficient.", "correct": False, "feedback": "Market data is not part of a blockchain explorer's core function of verifying on-chain data."}
        ],
        "project_link": "https://github.com/saumyasanghvi03/BlockVista-Terminal"
    },
    {
        "title": "The New Financial Product",
        "description": "A financial institution wants to launch a new, complex financial product that combines elements of a stock, an option, and a bond. They need to stress-test the product's performance under various market conditions, from a severe economic recession to a bull market.",
        "choices": [
            {"text": "A. It would provide a simplified risk-reward analysis based on historical asset prices, offering a broad overview.", "correct": False, "feedback": "Historical data is insufficient for a complex, forward-looking product."},
            {"text": "B. It would simulate the product's cash flows and returns across thousands of possible future market scenarios using Monte Carlo simulation.", "correct": True, "feedback": "Correct. **Monte Carlo simulation** is the industry standard for stress-testing complex financial products and is a core feature of advanced financial engineering platforms like **DerivX**."},
            {"text": "C. It would connect to a central bank's live data feed to predict market movements over the next year, ensuring the product is launched at the optimal time.", "correct": False, "feedback": "No financial model can accurately predict future market movements, and platforms like **DerivX** are for modeling, not prediction."}
        ],
        "project_link": "https://github.com/saumyasanghvi03/DerivX"
    },
    {
        "title": "The Treasury's Interest Rate Risk",
        "description": "A corporate treasury team needs to hedge against a potential sharp rise in interest rates, which would increase the cost of their variable-rate loans. They want a tailored, over-the-counter (OTC) solution that is not available on public exchanges.",
        "choices": [
            {"text": "A. Its capability to trade standardized futures contracts on a public exchange.", "correct": False, "feedback": "This would not be a tailored, OTC solution."},
            {"text": "B. The ability to model and price a customized **interest rate swap**, allowing them to exchange their variable-rate interest payments for fixed-rate payments.", "correct": True, "feedback": "Correct. An **interest rate swap** is the perfect OTC tool for this type of hedging, and a platform like **DerivX** would be used to model its terms."},
            {"text": "C. The system's liquidity-providing feature, which allows them to raise capital to pay off their loans.", "correct": False, "feedback": "The goal is to hedge, not to pay off the loan. This option does not address the core problem."}
        ],
        "project_link": "https://github.com/saumyasanghvi03/DerivX"
    }
]
