# Trading

## nasdaq subdirectory
Download, ingest, parse, summarise, analyse NASDAQ ITCH data.

"Nasdaq TotalView-ITCH — the standard Nasdaq data feed for serious traders — displays the full order book depth for Nasdaq market participants. TotalView also disseminates the Net Order Imbalance Indicator (NOII) for the Nasdaq Opening and Closing Crosses and Nasdaq IPO/Halt Cross."

### HFT Terminology:
Co-Location
Locating computers owned by HFT firms and proprietary traders in the same premises where an exchange’s computer servers are housed. This enables HFT firms to access stock prices a split second before the rest of the investing public. Co-location has become a lucrative business for exchanges, which charge HFT firms millions of dollars for the privilege of “low latency access.” 

As Michael Lewis explains in his book Flash Boys, the huge demand for co-location is a major reason why some stock exchanges have expanded their data centers substantially. While the old New York Stock Exchange building occupied 46,000 square feet, the NYSE data center in Mahwah, New Jersey, is almost nine times larger, at 400,000 square feet.

Flash Trading
A type of HFT trading wherein an exchange will “flash” information about buy and sell orders from market participants to HFT firms for a few fractions of a second before the information is made available to the public. Flash trading is controversial because HFT firms can use this information edge to trade ahead of pending orders, which can be construed as front running.

U.S. Senator Charles Schumer had urged the Securities and Exchange Commission in July 2009 to ban flash trading, saying that it created a two-tiered system where a privileged group received preferential treatment, while retail and institutional investors were put at an unfair disadvantage and deprived of a fair price for their transactions.

Latency
The time that elapses from the moment a signal is sent to its receipt. Since lower latency equals faster speed, high-frequency traders spend heavily to obtain the fastest computer hardware, software, and data lines so as execute orders as speedily as possible and gain a competitive edge in trading.

The biggest determinant of latency is the distance that the signal has to travel or the length of the physical cable (usually fiber-optic) that carries data from one point to another. Since light in a vacuum travels at 186,000 miles per second or 186 miles per millisecond, an HFT firm with its servers co-located right within an exchange would have a much lower latency—and hence a trading edge—than a rival firm located miles away.

Interestingly, an exchange’s co-location clients receive the same amount of cable length regardless of where they are located within the exchange premises, so as to ensure that they have the same latency. 

Liquidity Rebates
Most exchanges have adopted a “maker-taker model” for subsidizing the provision of stock liquidity. In this model, investors and traders who put in limit orders typically receive a small rebate from the exchange upon execution of their orders because they are regarded as having contributed to liquidity in the stock, i.e. they are liquidity “makers.”

Conversely, those who put in market orders are regarded as “takers” of liquidity and are charged a modest fee by the exchange for their orders. While the rebates are typically fractions of a cent per share, they can add up to significant amounts over the millions of shares traded daily by high-frequency traders. Many HFT firms employ trading strategies specifically designed to capture as much of the liquidity rebates as possible.

Matching Engine
The software algorithm that forms the nucleus of an exchange’s trading system and continuously matches buy and sell orders, a function previously performed by specialists on the trading floor. Since the matching engine matches buyers and sellers for all stocks, it is of vital importance for ensuring the smooth functioning of an exchange. The matching engine resides in the exchange’s computers and is the primary reason why HFT firms try to be in as close proximity to the exchange servers as they possibly can. 

Pinging
Refers to the tactic of entering small marketable orders—usually for 100 shares—in order to learn about large hidden orders in dark pools or exchanges. While you can think of pinging as being analogous to a ship or submarine sending out sonar signals to detect upcoming obstructions or enemy vessels, in the HFT context, pinging is used to find hidden "prey."

Here's how: buy-side firms use algorithmic trading systems to break up large orders into much smaller ones and feed them steadily into the market so as to reduce the market impact of large orders. In order to detect the presence of such large orders, HFT firms place bids and offer in 100-share lots for every listed stock.

Once a firm gets a “ping” (i.e., the HFT’s small order is executed) or series of pings that alerts the HFT to the presence of a large buy-side order, it may engage in a predatory trading activity that ensures it a nearly risk-free profit at the expense of the buy-sider, who will end up receiving an unfavorable price for its large order. Pinging has been likened to “baiting” by some influential market players since its sole purpose is to lure institutions with large orders to reveal their hand.

Point of Presence
The point where traders connect to the market exchange. In order to reduce latency, the goal of HFT firms is to get as close to the point of presence as possible. Also, see “Co-location.”

Predatory Trading
Trading practices employed by some high-frequency traders to make nearly risk-free profits at the expense of investors. In Lewis’ book, the IEX exchange, which seeks to combat some of the shadier HFT practices, identifies three activities that constitute predatory trading:

“Slow market arbitrage” or “latency arbitrage,” in which a high-frequency trader arbitrages minute price differences of stocks between various exchanges.
“Electronic front running,” which involves a HFT firm racing ahead of a large client order on an exchange, scooping up all the shares on offer at various other exchanges (if it is a buy order) or hitting all the bids (if it is a sell order), and then turning around and selling them to (or buying them from) the client and pocketing the difference.
“Rebate arbitrage” involves HFT activity that attempts to capture liquidity rebates offered by exchanges without really contributing to liquidity. Also, see “Liquidity Rebates.”


Securities Information Processor
The technology used to collect quotes and trade data from different exchanges, collate and consolidate that data, and continuously disseminate real-time price quotes and trades for all stocks. The SIP calculates the National Best Bid and Offer (NBBO) for all stocks, but because of the sheer volume of data, it has to handle, has a finite latency period.

A SIP’s latency in calculating the NBBO is generally higher than that of HFT firms (because of the latter’s faster computers and co-location), and it is this difference in latency—estimated by Lewis to occasionally reach as much as 25 milliseconds—that is at the core of predatory HFT activity.
The Consolidated Tape Association oversees the SIP for NYSE securities, while the UTP Plan does the same for Nasdaq stocks.

Smart Routers
Technology that determines to which exchanges orders or trades are sent. Smart routers can be programmed to send out pieces of large orders (after they are broken up by a trading algorithm) so as to get cost-effective trade execution. A smart router like a sequential cost-effective router may direct an order to a dark pool and then to a market exchange (if it is not executed in the former), or to an exchange where it is more likely to receive a liquidity rebate.
