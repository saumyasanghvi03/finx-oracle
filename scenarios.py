SCENARIOS = [
    {
        "title": "The Crypto Exchange Heist",
        "description": "Your AI-powered fraud detection system, **finAIguard**, flags a series of suspicious transactions. A new user, with a fresh wallet, is attempting to withdraw a massive sum received from a Tornado Cash mixer. Do you: ",
        "choices": [
            {
                "text": "A) **Flag & Freeze:** Immediately flag the transaction and freeze the account. This might disrupt a legitimate user but prevents a potential crime.",
                "correct": True,
                "feedback": "Correct. This aligns with **AML (Anti-Money Laundering)** best practices, as identified by our on-chain analytics. Your action saved the firm from a major compliance risk."
            },
            {
                "text": "B) **Wait & Watch:** Monitor the user's activity for 24 hours. A hasty freeze could lead to a user experience issue and lose a potential client.",
                "correct": False,
                "feedback": "Incorrect. In the world of on-chain forensics, speed is critical. Waiting could allow the funds to be moved through multiple wallets, making them unrecoverable."
            }
        ],
        "project_link": "https://github.com/saumyasanghvi03/onchain-aml-dashboard"
    },
    {
        "title": "The Derivatives Dilemma",
        "description": "A new hedge fund manager wants to hedge against a potential downturn in the S&P 500. Using your **DerivX** platform, they want to execute a complex options strategy. You must advise them on the right tool. What's your next move?",
        "choices": [
            {
                "text": "A) **Model it with Black-Scholes:** Recommend using a model like Black-Scholes to price the options accurately and understand potential outcomes.",
                "correct": True,
                "feedback": "Correct. The **Blockscholes** model provides a foundational framework for pricing complex options, enabling better strategic decisions and risk management."
            },
            {
                "text": "B) **Go with a simple future:** Advise them to use a simpler futures contract. It's less complex and easier to manage.",
                "correct": False,
                "feedback": "Incorrect. While simpler, a future lacks the strategic flexibility and targeted risk management that a well-structured options strategy provides."
            }
        ],
        "project_link": "https://github.com/saumyasanghvi03/DerivX"
    },
    {
        "title": "The On-Chain Sleuth",
        "description": "A well-known cryptocurrency exchange has just been hacked. You are tasked with tracing the stolen funds. Where do you start your investigation?",
        "choices": [
            {
                "text": "A) **Social Media Buzz:** Check Twitter and Reddit for clues from the crypto community.",
                "correct": False,
                "feedback": "Incorrect. While social media can offer clues, the most reliable data is on-chain. You need hard evidence, not speculation."
            },
            {
                "text": "B) **The Blockchain Explorer:** Use a **BlockVista Terminal** to trace the stolen funds from the point of origin, following each transaction hop.",
                "correct": True,
                "feedback": "Correct. The blockchain never lies. Using a terminal-based explorer is the most efficient and direct way to follow the money trail."
            }
        ],
        "project_link": "https://github.com/saumyasanghvi03/BlockVista-Terminal"
    }
]
