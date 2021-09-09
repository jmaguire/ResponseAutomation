# ResponseAutomation
Playground for assessment recommendations and other response automation techniques.

Uses sentence transformers from https://www.sbert.net/index.html and defaults to an asymmetric semantic search (short query can match long result).

## Usage
1. Install the requirements and run setup.py

2. Navigate to recommendation_engine because lazy

``` cd recommendation_engine ```

3. Run recommendations.py

``` python3 recommendations.py ```

4. Enter search text and see results

```
Enter question text: data security policy
47.5%: Do you have a data security policy? If yes, please attach or provide details.
46.1%: In the last 12 months have there been any changes in the formal data protection policy in relation to sharing of data with other business units and /or third parties/affiliates?
46.1%: Is data centre access limited to employees with appropriate job responsibilities?
42.6%: For cloud technology and associated cybersecurity risks, please confirm:
(i) that you have procedures and controls in place to protect our information from mishandling and  theft;
41.4%: Are you required to report data breaches to your regulators?
```
