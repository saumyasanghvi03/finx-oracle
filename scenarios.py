# In scenarios.py

SCENARIOS = [
    {
        "title": "AI Stock Prediction",
        "description": "An AI model you built predicts a 20% surge in a tech stock. Market sentiment is bearish. What's your move?",
        "project_link": "https://www.investopedia.com/terms/q/quantitativeanalysis.asp",
        "choices": [
            {"text": "Short the stock based on market sentiment.", "correct": False, "feedback": "Going against your data-driven model was a mistake. Market sentiment is often a lagging indicator."},
            {"text": "Buy call options to leverage the predicted upside.", "correct": True, "feedback": "Trusting your quantitative model over herd mentality is key to generating alpha."},
            {"text": "Do nothing and wait for more confirmation.", "correct": False, "feedback": "Analysis paralysis. Indecision led to a missed opportunity as the stock surged."},
            {"text": "Buy the stock with a tight stop-loss.", "correct": False, "feedback": "A reasonable but less optimal move. The volatility might have triggered your stop-loss before the main upward move."}
        ]
    },
    {
        "title": "Crypto Arbitrage Opportunity",
        "description": "You spot a 3% price difference for Bitcoin between two exchanges. Exchange A is cheaper. The network is congested, meaning higher fees and slower transfers.",
        "project_link": "https://www.investopedia.com/terms/a/arbitrage.asp",
        "choices": [
            {"text": "Ignore the opportunity; it's too risky with network congestion.", "correct": False, "feedback": "While risky, a 3% arbitrage is significant. A good trader would quantify the risk vs. reward."},
            {"text": "Execute the trade immediately, buying on Exchange A and selling on B.", "correct": False, "feedback": "Acting too fast without accounting for fees was a mistake. The high fees ate up your entire profit margin."},
            {"text": "Calculate the potential profit after factoring in maximum potential network fees.", "correct": True, "feedback": "Excellent. You quantified your execution risk. After calculation, the trade was still profitable."},
            {"text": "Market-make on the more expensive exchange to capture the spread.", "correct": False, "feedback": "This is a different strategy and doesn't directly address the immediate arbitrage opportunity."}
        ]
    },
    {
        "title": "Earnings Report Surprise",
        "description": "A company is expected to miss earnings estimates. However, your channel checks suggest a surprise beat. Implied volatility is extremely high.",
        "project_link": "https://www.investopedia.com/terms/i/iv.asp",
        "choices": [
            {"text": "Buy OTM (Out-of-the-Money) calls, hoping for a massive price spike.", "correct": False, "feedback": "The high implied volatility means options are extremely expensive. Even if you were right, 'IV crush' after earnings could lead to a loss."},
            {"text": "Short the stock, following the market consensus.", "correct": False, "feedback": "Following the herd without your own research is a recipe for disaster. The stock soared on the earnings beat."},
            {"text": "Sell puts or a put spread to collect the high premium.", "correct": True, "feedback": "This is a great strategy. You took advantage of the high IV and had a bullish view. You profit from the premium decay and the stock moving up."},
            {"text": "Buy the stock outright before the report.", "correct": False, "feedback": "Too risky. An earnings miss would have resulted in a significant loss. Selling options was a more risk-defined strategy."}
        ]
    },
    {
        "title": "DeFi Protocol Hack",
        "description": "A major DeFi lending protocol's governance token (GOV) has plummeted 50% due to a suspected hack and exploit. The developers are about to issue a statement.",
        "project_link": "https://www.investopedia.com/decentralized-finance-defi-5113835",
        "choices": [
            {"text": "Buy the dip. The token is cheap and will surely recover.", "correct": False, "feedback": "This is catching a falling knife. Without knowing the extent of the damage, this is pure gambling."},
            {"text": "Short the token, expecting it to go to zero.", "correct": False, "feedback": "While possible, the bad news may already be priced in. You risk a 'short squeeze' if the news is better than expected."},
            {"text": "Wait for the official statement and assess if the treasury was drained.", "correct": True, "feedback": "Perfect. You avoided emotional decision-making and waited for fundamental information. The statement revealed funds were safe, causing a massive recovery."},
            {"text": "Invest in a rival protocol's token.", "correct": False, "feedback": "While this might be a valid long-term thesis, it doesn't capitalize on the immediate volatility and information event of the hacked protocol."}
        ]
    },
    {
        "title": "Federal Reserve Interest Rate Decision",
        "description": "The market has priced in a 95% chance of a 25 bps rate hike. Your economic model suggests a surprise 'no hike' decision is more likely.",
        "project_link": "https://www.investopedia.com/terms/f/federalreservebank.asp",
        "choices": [
            {"text": "Go long on bonds, which rally when rate hikes don't happen.", "correct": True, "feedback": "A classic contrarian trade based on your model. When the Fed announced no hike, bonds soared and you locked in a significant profit."},
            {"text": "Short bonds, in line with the overwhelming market expectation.", "correct": False, "feedback": "The market had already priced this in. Your risk/reward was highly asymmetrical and skewed against you."},
            {"text": "Do nothing. It's impossible to predict the Fed.", "correct": False, "feedback": "While difficult, your job as a trader is to act on well-founded, asymmetrical bets. Your model gave you an edge you didn't use."},
            {"text": "Go long on the US Dollar, which strengthens with rate hikes.", "correct": False, "feedback": "You traded based on the consensus, not your own analysis. The dollar fell when the surprise 'no hike' decision was announced."}
        ]
    }
]
