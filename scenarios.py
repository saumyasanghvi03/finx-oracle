SCENARIOS = [
    # **finAIguard (AI in Financial Security)**
    {
        "title": "The Crypto Exchange Heist",
        "description": "Your AI-driven fraud detection system, **finAIguard**, flags an anomaly. A long-standing, high-net-worth client with a history of steady, large-sum transactions suddenly initiates a series of 50 small, identical transfers to 50 different, previously unknown recipients in various jurisdictions over a span of 30 minutes. The total value is significant.",
        "choices": [
            {"text": "A. Immediately decline all transfers and freeze the client's account, citing a high-risk security alert.", "correct": False, "feedback": "An immediate freeze is too aggressive for an established client and could lead to a customer service crisis. Behavioral analysis is a better first step."},
            {"text": "B. Soft-flag the account and trigger an internal review, while simultaneously implementing a **behavioral analytics model** to compare this new pattern against the client's historical data for real-time risk scoring.", "correct": True, "feedback": "Correct. This is a balanced, AI-driven approach. It avoids a public-facing service disruption while using advanced analytics to determine the true risk."},
            {"text": "C. Automatically approve the first transfer to avoid service disruption and flag the remaining 49 for manual review.", "correct": False, "feedback": "This is a poor security practice; it allows the initial portion of a potentially fraudulent transaction to go through."}
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
        "title": "The Insider Trading Red Flag",
        "description": "An employee at a large investment firm has started making suspiciously well-timed trades just before major market-moving announcements. Your AI system flags their personal trading activity as anomalous. How does **finAIguard** handle this?",
        "choices": [
            {"text": "A. Automatically report the employee to the SEC.", "correct": False, "feedback": "While a serious flag, an automatic report could lead to legal issues. You need a more deliberate approach."},
            {"text": "B. Use a **graph-based machine learning model** to analyze the employee's communication and social network data for connections to key decision-makers.", "correct": True, "feedback": "Correct. Graph models are excellent for identifying hidden connections and patterns in complex networks, which is crucial for insider trading detection."},
            {"text": "C. Flag the employee's trades for manual review without providing any context on why they are suspicious.", "correct": False, "feedback": "This is insufficient. A good AI system provides a clear rationale for its flags to assist human reviewers."}
        ],
        "project_link": "https://github.com/saumyasanghvi03/finAIguard"
    },
    {
        "title": "The Black Box Conundrum",
        "description": "A major bank's risk department is hesitant to adopt your AI model for credit scoring because they cannot explain how it arrives at its decisions, making it a 'black box.' They demand more transparency.",
        "choices": [
            {"text": "A. Implement a **Local Interpretable Model-agnostic Explanations (LIME)** feature to explain individual predictions.", "correct": True, "feedback": "Correct. LIME provides a simple, interpretable explanation for any machine learning model's prediction, solving the 'black box' problem."},
            {"text": "B. Revert the AI model to a simpler, rule-based system for full transparency.", "correct": False, "feedback": "This would sacrifice the accuracy and power of the AI model for simplicity, which is a step backward."},
            {"text": "C. Tell the risk department that AI models are inherently unexplainable.", "correct": False, "feedback": "This is an outdated view. Modern AI tools focus on explainability to build trust with human experts."}
        ],
        "project_link": "https://github.com/saumyasanghvi03/finAIguard"
    },

    # **onchain-aml-dashboard (On-Chain AML)**
    {
        "title": "The On-Chain Laundering Scheme",
        "description": "You are a compliance officer at a major cryptocurrency exchange. Your **onchain-aml-dashboard** identifies a user who has just deposited a large amount of a popular stablecoin. The funds originated from a complex series of transactions involving a privacy-enhancing mixer service, a series of low-value dust attacks on other wallets, and a final consolidation through a decentralized exchange (DEX).",
        "choices": [
            {"text": "A. Immediately file a Suspicious Activity Report (SAR) with the relevant financial authorities.", "correct": False, "feedback": "An immediate SAR can be premature and damage a user's reputation. You need more data first."},
            {"text": "B. Initiate an enhanced due diligence (EDD) review of the user, while flagging the transaction for further analysis to determine if the pattern is part of a larger, illicit network.", "correct": True, "feedback": "Correct. The pattern of mixers, dust attacks, and DEX swaps is highly indicative of layering, a stage in money laundering. This action aligns with the purpose of an **onchain-aml-dashboard**."},
            {"text": "C. Approve the transaction without a red flag, as the funds are now in a stablecoin.", "correct": False, "feedback": "The asset type doesn't absolve the transaction's history. The source of funds is the key factor, not the final asset."}
        ],
        "project_link": "https://github.com/saumyasanghvi03/onchain-aml-dashboard"
    },
    {
        "title": "The DeFi Protocol Audit",
        "description": "A decentralized finance (DeFi) protocol wants to ensure it is not being used for illicit activities. They need a way to monitor transactions without compromising the privacy of their users.",
        "choices": [
            {"text": "A. **Token-specific risk scoring** that assigns a risk rating to a user's wallet based on its interaction with high-risk tokens.", "correct": False, "feedback": "This is a useful feature but doesn't address the core problem of identifying complex, multi-wallet schemes."},
            {"text": "B. An **address clustering** tool that groups wallets based on their transactional behavior to identify patterns of layering and fund commingling.", "correct": True, "feedback": "Correct. **Address clustering** is the key feature of a professional on-chain AML dashboard. It helps link seemingly unrelated wallets to a single user or group, uncovering large-scale money laundering networks."},
            {"text": "C. A **zero-knowledge proof (ZKP)**-based system that verifies the legitimacy of a user's funds without revealing their transaction history.", "correct": False, "feedback": "While a ZKP system can be used for compliance, its primary use is for privacy, not for identifying illicit fund flows after the fact."}
        ],
        "project_link": "https://github.com/saumyasanghvi03/onchain-aml-dashboard"
    },
    {
        "title": "The Wash Trading Loop",
        "description": "A new NFT project has an unusually high trading volume between a small number of wallets, driving up the perceived value. Your on-chain analytics dashboard must identify this behavior, known as 'wash trading.'",
        "choices": [
            {"text": "A. Look for a large number of transactions originating from a single wallet in a short period of time.", "correct": False, "feedback": "This can indicate legitimate trading activity. You need a more sophisticated method."},
            {"text": "B. Identify transaction loops where a token or NFT is sold back and forth between a small cluster of wallets.", "correct": True, "feedback": "Correct. Identifying these closed transaction loops is the definitive way to detect wash trading, a key feature of an advanced on-chain dashboard."},
            {"text": "C. Flag all transactions involving more than two wallets.", "correct": False, "feedback": "This would generate a massive number of false positives, as most legitimate transactions involve multiple wallets."}
        ],
        "project_link": "https://github.com/saumyasanghvi03/onchain-aml-dashboard"
    },
    {
        "title": "The Transaction Graph",
        "description": "You are assessing the risk of a new DeFi protocol. Your dashboard reveals a complex web of transactions involving the protocol's main liquidity pool. Some of the interacting addresses have been flagged for illicit activity in the past, but the current transactions are not directly linked. You must still assess the risk.",
        "choices": [
            {"text": "A. Use **graph-based risk analysis** to measure the 'hops' or distance between the flagged addresses and the protocol's liquidity pool.", "correct": True, "feedback": "Correct. Graph analysis is crucial for understanding the indirect risk exposure of a protocol. It shows how close a clean entity is to a 'dirty' one."},
            {"text": "B. Ignore the connections since the transactions are not direct.", "correct": False, "feedback": "This is a dangerous approach. Illicit funds are often moved through multiple layers to obscure their origin."},
            {"text": "C. Flag the protocol itself as high-risk regardless of the specific addresses.", "correct": False, "feedback": "This is a blunt and unfair assessment. You need to identify the specific sources of risk, not condemn the entire protocol."}
        ],
        "project_link": "https://github.com/saumyasanghvi03/onchain-aml-dashboard"
    },

    # **blockscholes / DerivX (Derivatives & Options Trading)**
    {
        "title": "The Derivatives Dilemma",
        "description": "A portfolio manager holds a significant position in a volatile tech stock. They are concerned about a potential short-term price drop but do not want to sell their shares. They are looking for a way to mitigate this downside risk while still retaining ownership.",
        "choices": [
            {"text": "A. Execute a **futures contract** to sell the stock at a future date.", "correct": False, "feedback": "A futures contract is a binding agreement to sell, which would force them to sell their shares."},
            {"text": "B. Purchase a **put option**, which gives them the right, but not the obligation, to sell the stock at a pre-determined price if the market falls.", "correct": True, "feedback": "Correct. A **put option** is the classic hedging strategy for a long position, as it provides protection against a price drop without forcing a sale."},
            {"text": "C. Initiate a **covered call strategy**, which involves selling a call option to generate income from the stock's potential upside.", "correct": False, "feedback": "A covered call is an income-generating strategy, but it does not protect against downside risk."}
        ],
        "project_link": "https://github.com/saumyasanghvi03/DerivX"
    },
    {
        "title": "The Quant's Leverage",
        "description": "A quantitative trader believes a stock is undervalued but needs to leverage a small amount of capital to maximize potential gains. They want to bet on a significant price increase in the next month, with limited downside risk if they are wrong.",
        "choices": [
            {"text": "A. It would provide the probability of the stock reaching a certain price, helping them decide which strike price to choose for a **call option**.", "correct": True, "feedback": "Correct. The **blockscholes** model is foundational for pricing options. By analyzing the variables, it helps a trader choose the optimal strike price to maximize leverage."},
            {"text": "B. It would calculate the fair value of a **put option**, allowing them to determine if it is overpriced for an arbitrage opportunity.", "correct": False, "feedback": "While the model can do this, it doesn't align with the trader's goal of leveraging a bullish bet."},
            {"text": "C. It would generate a real-time volatility index for the stock.", "correct": False, "feedback": "The model uses volatility as an input, but generating a real-time volatility index is a different function."}
        ],
        "project_link": "https://github.com/saumyasanghvi03/blockscholes"
    },
    {
        "title": "The Volatility Smile",
        "description": "A trader notices that out-of-the-money options for a particular stock are priced higher than what the standard **Black-Scholes model** predicts. This discrepancy is known as a 'volatility smile.' What is the most likely reason for this?",
        "choices": [
            {"text": "A. The model is flawed and cannot price options accurately.", "correct": False, "feedback": "The model has known limitations, but it is still the industry standard for its assumptions."},
            {"text": "B. The market is pricing in a higher probability of extreme events (tail risk) that the Black-Scholes model does not account for.", "correct": True, "feedback": "Correct. The volatility smile is a direct result of market participants pricing in tail risk, which the original **Black-Scholes** model, with its assumption of log-normal returns, does not capture."},
            {"text": "C. The stock is about to undergo a stock split.", "correct": False, "feedback": "A stock split does not directly affect the pricing of out-of-the-money options in this way."},
            {"text": "D. There is an arbitrage opportunity.", "correct": False, "feedback": "While arbitrage might be possible, the volatility smile itself is not an arbitrage opportunity; it is a fundamental market observation."}
        ],
        "project_link": "https://github.com/saumyasanghvi03/blockscholes"
    },
    {
        "title": "The Options Spread Strategy",
        "description": "A trader is moderately bullish on a stock but wants to reduce the cost of buying a call option while also limiting their potential profits. Using the **DerivX** platform, what kind of options spread would they use?",
        "choices": [
            {"text": "A. A **bull call spread**, where they buy a call at a lower strike price and sell a call at a higher strike price.", "correct": True, "feedback": "Correct. A bull call spread is a perfect strategy for this scenario. Selling the higher-strike call finances the purchase of the lower-strike call, reducing the upfront cost and risk."},
            {"text": "B. A bear put spread, where they buy a put at a higher strike price and sell a put at a lower strike price.", "correct": False, "feedback": "This is a bearish strategy, not a bullish one."},
            {"text": "C. A straddle, which involves buying a call and a put at the same strike price.", "correct": False, "feedback": "A straddle is used when a trader expects high volatility, not a moderate price increase."}
        ],
        "project_link": "https://github.com/saumyasanghvi03/DerivX"
    },

    # **BlockVista-Terminal (Blockchain Explorers)**
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
        "title": "The Token Supply Audit",
        "description": "A new project's website claims a total token supply of 1 billion. As a diligent investor, you want to verify this on-chain and check for any unauthorized minting of new tokens.",
        "choices": [
            {"text": "A. Check a third-party market data aggregator for the token's total supply.", "correct": False, "feedback": "Third-party data can be manipulated. You must verify it on the blockchain."},
            {"text": "B. Use a **BlockVista Terminal** to query the smart contract's `totalSupply()` function and look for any minting events since the initial supply was created.", "correct": True, "feedback": "Correct. The most reliable way to audit a token's supply is to directly query the smart contract on the blockchain and inspect its event logs."},
            {"text": "C. Follow the project's official Twitter account for updates.", "correct": False, "feedback": "This is a social check, not an on-chain audit. It is highly susceptible to misinformation."}
        ],
        "project_link": "https://github.com/saumyasanghvi03/BlockVista-Terminal"
    },
    {
        "title": "The Market Manipulation Hunt",
        "description": "A token's price just experienced a dramatic, unexplained spike. Your theory is that a coordinated 'pump and dump' scheme is in progress. You need to use your **BlockVista Terminal** to confirm this.",
        "choices": [
            {"text": "A. Search for large, centralized exchange buy orders.", "correct": False, "feedback": "You can't see centralized exchange order books on the blockchain."},
            {"text": "B. Analyze the wallet addresses involved in the price spike, looking for a cluster of wallets funded by a single entity and their subsequent coordinated sales.", "correct": True, "feedback": "Correct. This is the classic on-chain pattern for a pump and dump. A **BlockVista Terminal** is the perfect tool for this type of behavioral analysis."},
            {"text": "C. Contact the project's founders for an explanation.", "correct": False, "feedback": "The founders are unlikely to admit to market manipulation. The evidence must be on-chain."}
        ],
        "project_link": "https://github.com/saumyasanghvi03/BlockVista-Terminal"
    },

    # **DerivX (Advanced Financial Engineering)**
    {
        "title": "The New Financial Product",
        "description": "A financial institution wants to launch a new, complex financial product that combines elements of a stock, an option, and a bond. They need to stress-test the product's performance under various market conditions, from a severe economic recession to a bull market.",
        "choices": [
            {"text": "A. It would provide a simplified risk-reward analysis based on historical asset prices, offering a broad overview.", "correct": False, "feedback": "Historical data is insufficient for a complex, forward-looking product."},
            {"text": "B. It would simulate the product's cash flows and returns across thousands of possible future market scenarios using Monte Carlo simulation.", "correct": True, "feedback": "Correct. **Monte Carlo simulation** is the industry standard for stress-testing complex financial products and is a core feature of advanced financial engineering platforms like **DerivX**."},
            {"text": "C. It would connect to a central bank's live data feed to predict market movements over the next year.", "correct": False, "feedback": "No financial model can accurately predict future market movements, and platforms like **DerivX** are for modeling, not prediction."}
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
    },
    {
        "title": "The Exotic Option Structuring",
        "description": "A savvy institutional client wants to hedge against a simultaneous drop in two different asset classes, such as a stock index and a specific commodity. They need a custom-built, multi-asset derivative product.",
        "choices": [
            {"text": "A. Recommend a simple portfolio of futures contracts.", "correct": False, "feedback": "A futures portfolio would require active management and cannot provide the integrated risk exposure they need."},
            {"text": "B. Use the **DerivX** platform to structure a custom **basket option** that depends on the performance of both underlying assets.", "correct": True, "feedback": "Correct. A basket option is an exotic derivative designed to manage risk across a 'basket' of assets, which is exactly what the client needs."},
            {"text": "C. Advise the client to simply sell both assets.", "correct": False, "feedback": "This would be a simple and often inefficient way to manage risk, and it goes against the client's desire for a derivative-based solution."}
        ],
        "project_link": "https://github.com/saumyasanghvi03/DerivX"
    },
    {
        "title": "The Quantitative Risk Assessment",
        "description": "A bank's internal quantitative team needs to assess the risk of its entire derivatives portfolio under a 'Black Swan' event, where all markets drop simultaneously. They need to calculate the **Value at Risk (VaR)** for the entire portfolio.",
        "choices": [
            {"text": "A. Use the **Black-Scholes model** to price each option individually and sum them up.", "correct": False, "feedback": "Black-Scholes prices options at a single point in time and doesn't account for complex, portfolio-wide risk."},
            {"text": "B. Run a **historical simulation** and a **parametric VaR model** on the entire portfolio to estimate potential losses at a specific confidence level.", "correct": True, "feedback": "Correct. VaR models are designed to measure potential losses under a variety of market conditions, making them ideal for this type of portfolio-level risk assessment."},
            {"text": "C. Hire an expert to manually review each derivative contract.", "correct": False, "feedback": "This is a time-consuming and inefficient method for a large portfolio. You need a quantitative, scalable solution."}
        ],
        "project_link": "https://github.com/saumyasanghvi03/DerivX"
    }
]
