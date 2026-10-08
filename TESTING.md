\# BlockTrace — Smart Contract Testing Results



\## 1. Testing Objective



The objective of testing was to verify that the BlockTrace smart contract could register food products, transfer ownership between supply chain participants, update product statuses, and retrieve information from a local Ethereum blockchain.



\## 2. Testing Environment



\- \*\*Smart Contract:\*\* Solidity 0.8.20

\- \*\*Development Environment:\*\* Remix IDE

\- \*\*Blockchain:\*\* Ganache

\- \*\*Chain ID:\*\* 1337

\- \*\*Application:\*\* Python with Web3.py

\- \*\*Product:\*\* Organic Coffee

\- \*\*Origin:\*\* Brazil



\## 3. Functional Test Results



| Test ID | Test Description | Expected Result | Observed Result | Status |

|---|---|---|---|---|

| T01 | Connect Python to Ganache | Successful connection | Connected to Ganache | Pass |

| T02 | Register Organic Coffee | Product ID generated | Product ID 1 created | Pass |

| T03 | Update product to Harvested | Status updated | Harvested recorded | Pass |

| T04 | Transfer to Distributor | Ownership changes | Distributor became owner | Pass |

| T05 | Update to In Transit | Status updated | In Transit recorded | Pass |

| T06 | Transfer to Retailer | Ownership changes | Retailer became owner | Pass |

| T07 | Update to Available for Sale | Final status recorded | Available for Sale recorded | Pass |

| T08 | Retrieve final product state | Correct product information | Product ID, name, origin, owner and status returned | Pass |

| T09 | Inspect Ganache blocks | Transactions recorded | Seven transaction-containing blocks observed | Pass |



\## 4. Testing Evidence



\- `screenshots/01-final-product-state.png` — Shows the final product information and successful retailer update.

\- `screenshots/02-ganache-transactions.png` — Shows the Ganache blockchain connection and transactions.



\## 5. Conclusion



The functional tests demonstrated that BlockTrace can track a food product through a simulated supply chain using Solidity, Ganache, Python and Web3.py.



The prototype successfully recorded ownership changes and product status updates on the local blockchain. Further testing is required for security, scalability, invalid inputs and real-world deployment.

