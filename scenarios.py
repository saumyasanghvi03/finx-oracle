# scenarios.py
import random

SCENARIOS = [
    {
        "title": "Fintech: 'Buy Now, Pay Later' (BNPL)",
        "description": "Which two statements are true about the primary business model of 'Buy Now, Pay Later' (BNPL) services?",
        "category": "fintech",
        "references": "- **Concept:** [Buy Now, Pay Later (BNPL)](https://www.investopedia.com/buy-now-pay-later-5182291)",
        "choices": [
            {"text": "They earn revenue from fees charged to merchants.", "correct": True, "feedback": "This is a primary revenue stream, as merchants pay a fee to offer the service and increase sales."},
            {"text": "They earn revenue from interest or late fees from consumers.", "correct": True, "feedback": "This is the other major revenue stream, collected from consumers who do not pay on time."},
            {"text": "They require all users to pay a monthly subscription.", "correct": False, "feedback": "Most BNPL services do not require subscriptions for basic use."},
            {"text": "They operate as fully-licensed traditional banks.", "correct": False, "feedback": "BNPL services are financial technology companies, not traditional banks."}
        ]
    },
    {
        "title": "Fintech: Robo-Advisors",
        "description": "What are two key advantages of using a 'Robo-Advisor' for investing?",
        "category": "fintech",
        "references": "- **Tool:** [Robo-Advisor](https://www.investopedia.com/terms/r/roboadvisor.asp)",
        "choices": [
            {"text": "Lower management fees compared to traditional human advisors.", "correct": True, "feedback": "Automation allows robo-advisors to operate with much lower overhead, resulting in lower fees."},
            {"text": "High accessibility with low minimum investment requirements.", "correct": True, "feedback": "They are designed to be accessible to a wide range of investors, often with very low or no minimums."},
            {"text": "They guarantee that your portfolio will never lose money.", "correct": False, "feedback": "No investment service can guarantee against losses, as all investments carry market risk."},
            {"text": "They provide complex, custom tax advice for high-net-worth clients.", "correct": False, "feedback": "While they may offer tax-loss harvesting, complex tax advice is typically outside their scope."}
        ]
    },
    {
        "title": "Fintech: Blockchain Technology",
        "description": "What are two fundamental features of blockchain technology?",
        "category": "fintech",
        "references": "- **Technology:** [Blockchain Explained](https://www.investopedia.com/terms/b/blockchain.asp)",
        "choices": [
            {"text": "It is a distributed ledger, meaning the record is shared across many computers.", "correct": True, "feedback": "This decentralization is key to its security and transparency."},
            {"text": "The records (blocks) are immutable, meaning they cannot be altered once added.", "correct": True, "feedback": "Immutability ensures the integrity of the transaction history."},
            {"text": "It is controlled by a single central authority, like a central bank.", "correct": False, "feedback": "Blockchain is designed to be decentralized, the opposite of having a central authority."},
            {"text": "It guarantees complete anonymity for all users.", "correct": False, "feedback": "While it can be pseudonymous, transactions on public blockchains are typically traceable."}
        ]
    },
    {
        "title": "Fintech: Peer-to-Peer (P2P) Lending",
        "description": "Which two statements accurately describe Peer-to-Peer (P2P) lending?",
        "category": "fintech",
        "references": "- **Concept:** [Peer-to-Peer (P2P) Lending](https://www.investopedia.com/terms/p/peer-to-peer-lending.asp)",
        "choices": [
            {"text": "It connects individual borrowers directly with individual investors (lenders).", "correct": True, "feedback": "This is the core function, bypassing traditional financial intermediaries like banks."},
            {"text": "Investors face the risk of borrower default.", "correct": True, "feedback": "Because there is no bank underwriting the risk, the individual investor bears the loss if a borrower defaults."},
            {"text": "All P2P loans are guaranteed by the government.", "correct": False, "feedback": "P2P loans are private investments and are not typically insured or guaranteed by the government."},
            {"text": "It is only used for obtaining large corporate business loans.", "correct": False, "feedback": "P2P lending is most commonly used for personal loans, not large corporate financing."}
        ]
    },
    {
        "title": "Fintech: Neobanks",
        "description": "What are two common characteristics of 'Neobanks'?",
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
        "description": "What are two key outcomes of 'Open Banking'?",
        "category": "fintech",
        "references": "- **Concept:** [Open Banking](https://www.investopedia.com/terms/o/open-banking.asp)",
        "choices": [
            {"text": "It allows third-party financial apps to access a user's bank data with their consent.", "correct": True, "feedback": "This is the primary mechanism, using secure APIs to share data."},
            {"text": "It fosters greater competition and innovation in financial services.", "correct": True, "feedback": "By allowing new fintech companies to build services on top of bank data, it creates more choices for consumers."},
            {"text": "It merges all of a user's bank accounts into a single government-controlled account.", "correct": False, "feedback": "Open Banking is about data sharing between private entities with user consent, not consolidation under government control."},
            {"text": "It eliminates the need for passwords by using only biometric authentication.", "correct": False, "feedback": "While biometrics are part of modern security, Open Banking's core function is data sharing via APIs, not changing authentication rules."}
        ]
    },
    {
        "title": "Fintech: Insurtech",
        "description": "Which two are common applications of 'Insurtech'?",
        "category": "fintech",
        "references": "- **Industry:** [Insurtech](https://www.investopedia.com/terms/i/insurtech.asp)",
        "choices": [
            {"text": "Using telematics data from a car to determine auto insurance premiums.", "correct": True, "feedback": "This is a prime example of using real-time data to price risk more accurately."},
            {"text": "Using health data from wearables to offer personalized life insurance rates.", "correct": True, "feedback": "This allows insurers to reward healthy lifestyles with lower premiums."},
            {"text": "Replacing all human insurance agents with robots.", "correct": False, "feedback": "While Insurtech automates many processes, human agents still play a key role, especially for complex products."},
            {"text": "Creating a single insurance policy that covers every possible risk in the world.", "correct": False, "feedback": "Insurtech focuses on personalizing and specializing insurance, not creating a universal, one-size-fits-all policy."}
        ]
    },
    {
        "title": "Fintech: Crowdfunding",
        "description": "What are two distinct types of crowdfunding?",
        "category": "fintech",
        "references": "- **Concept:** [Crowdfunding](https://www.investopedia.com/terms/c/crowdfunding.asp)",
        "choices": [
            {"text": "Reward-based crowdfunding, where backers get a product or perk.", "correct": True, "feedback": "This is common on platforms like Kickstarter, where you get the product you helped fund."},
            {"text": "Equity crowdfunding, where backers receive a stake or ownership in the company.", "correct": True, "feedback": "This is common on platforms like SeedInvest, where backers become investors in the business."},
            {"text": "Tax-based crowdfunding, where backers pay a company's taxes.", "correct": False, "feedback": "This is not a recognized model of crowdfunding."},
            {"text": "Political crowdfunding, where the funds are used exclusively to lobby governments.", "correct": False, "feedback": "While political fundraising exists, it's distinct from the business and project-based models of crowdfunding."}
        ]
    },
    {
        "title": "Fintech: Staking in Crypto",
        "description": "In a Proof-of-Stake (PoS) system, what are two purposes of 'staking' cryptocurrency?",
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
        "title": "Stock Market: Market Capitalization",
        "description": "Which two statements about 'Market Capitalization' are correct?",
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
        "description": "Which two definitions are correct?",
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
        "description": "What are two valid interpretations of a high Price-to-Earnings (P/E) ratio?",
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
        "description": "Which two statements correctly differentiate ETFs from Mutual Funds?",
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
        "description": "Which two are true statements about stock dividends?",
        "category": "general_finance",
        "references": "- **Concept:** [Dividend](https://www.investopedia.com/terms/d/dividend.asp)",
        "choices": [
            {"text": "They are a way for a company to distribute its profits to shareholders.", "correct": True, "feedback": "This is the definition of a dividend—a reward to the owners of the company."},
            {"text": "Companies are not legally obligated to pay dividends.", "correct": True, "feedback": "A company's board of directors decides whether to pay a dividend; it is not a requirement."},
            {"text": "The dividend payment causes the company's stock price to increase.", "correct": False, "feedback": "On the ex-dividend date, the stock price typically drops by the amount of the dividend, as that cash is no longer part of the company's value."},
            {"text": "Only technology companies are allowed to pay dividends.", "correct": False, "feedback": "Companies in any industry can pay dividends, and they are most common among mature, stable companies."}
        ]
    },
    {
        "title": "Stock Market: Short Selling",
        "description": "What are two significant risks associated with 'short selling' a stock?",
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
        "description": "Which two descriptions apply to 'blue-chip' stocks but NOT to 'penny stocks'?",
        "category": "general_finance",
        "references": "- **Concept:** [Blue-Chip Stock](https://www.investopedia.com/terms/b/bluechipstock.asp)",
        "choices": [
            {"text": "They are large, financially sound companies with a history of reliability.", "correct": True, "feedback": "This is the definition of a blue-chip stock."},
            {"text": "They often pay regular dividends to shareholders.", "correct": True, "feedback": "Their stable cash flows allow many blue-chip companies to pay consistent dividends."},
            {"text": "They are highly speculative and have a high risk of failure.", "correct": False, "feedback": "This describes penny stocks, not blue-chip stocks."},
            {"text": "They trade for very low prices, often less than $5 per share.", "correct": False, "feedback": "This is the definition of a penny stock."}
        ]
    },
    {
        "title": "Stock Market: Market Order vs. Limit Order",
        "description": "Which two statements accurately describe order types?",
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
        "description": "Which two of the following are examples of diversification?",
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
        "description": "What two factors have the greatest impact on the power of compound interest?",
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
        "description": "Which two actions are most likely to improve your credit score?",
        "category": "general_finance",
        "references": "- **Metric:** [Credit Score](https://www.investopedia.com/terms/c/credit_score.asp)",
        "choices": [
            {"text": "Making all of your payments on time.", "correct": True, "feedback": "Payment history is the single most important factor in a credit score."},
            {"text": "Keeping your credit card balances low relative to their limits.", "correct": True, "feedback": "This is known as your credit utilization ratio, and keeping it low is very important."},
            {"text": "Closing all of your old credit card accounts.", "correct": False, "feedback": "This can actually hurt your score by reducing your average age of accounts and increasing your utilization ratio."},
            {"text": "Checking your credit score every single day.", "correct": False, "feedback": "Checking your own score (a 'soft inquiry') does not affect it, but it also doesn't improve it."}
        ]
    },
    {
        "title": "General Finance: Inflation",
        "description": "Which two asset classes have historically performed well during periods of high inflation?",
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
        "description": "In the event of a company's bankruptcy, which two statements are true?",
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
        "description": "Which two items are considered liabilities when calculating your net worth?",
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
        "description": "Which two are key characteristics of a proper 'emergency fund'?",
        "category": "general_finance",
        "references": "- **Concept:** [Emergency Fund](https://www.investopedia.com/terms/e/emergency_fund.asp)",
        "choices": [
            {"text": "It should be liquid, meaning easily accessible as cash.", "correct": True, "feedback": "The money needs to be available immediately, so a high-yield savings account is a common choice."},
            {"text": "It should typically cover 3-6 months of essential living expenses.", "correct": True, "feedback": "This is the standard financial planning advice to provide a cushion in case of job loss or other emergencies."},
            {"text": "It should be invested in high-growth technology stocks.", "correct": False, "feedback": "This would expose your emergency savings to market risk, defeating its purpose as a safety net."},
            {"text": "It should be used for planned expenses like vacations.", "correct": False, "feedback": "An emergency fund is strictly for unplanned, urgent financial needs."}
        ]
    }
]
