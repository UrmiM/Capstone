### User Activity Data Analysis for SalesTech StartUp ELTROPY

## A little about ELTROPY
Eltropy empowers financial services companies to engage clients and sell financial products over Text Messaging.
A once-in-a-generation communication revolution is underway: a shift from emails, phone calls to Messaging. 95% of text messages are opened and read within 3 minutes, and responded to within 90 seconds.
Eltropy’s technology allows client-facing teams to leverage Messaging platforms like iMessage, SMS, Facebook Messenger etc. to engage prospects and clients in a whole new way. Which results in an 11x increase in client engagement and Sales conversion metrics.

## Data as a door to find customers' behavior
What does the data tell us?
Does the behavior of the customer differ based on geographical locations, industry type, time of day, day of week, month?
Can we identify on-the-fence customers? How soon can we do that?
Are there any underlying "View" patterns specific to a certain industry type? Can we generalize for all?
Can we use insights from one industry for another?
What can help the business leaders in focusing and prioritizing efforts and brain power?
Recommendation for future data collection efforts.

## Data Format
Data was from four customers of Eltropy, from varying industries, of user activities "Share" and "View". The data had about 12 features, all but one ("Time spent in seconds") being categorical features. Each row is an activity. The features being in the following format.
![alt text][logo]
[logo]: https://github.com/UrmiM/Capstone/Data/Data_Format_Example

## Truth about the Data
..* The data has 6000 rows but information is for only 600 users. It is not possible to get good predictions since no information is available about the content. The only feature with good signal is "Time Spent In Seconds".
..* Also, there is no conversion data, therefore classification was not possible.
..* Linear Regression was implemented to predict the "Time Spent per View" with dummified features for month, day of week, viewing device, browser type, time of day etc. but the r2 for the model is very low.
..* Random Forest Regressor was implemented as well for the same feature set, but there was no improvement seen in the prediction. Cross Validation using the train_test_split.
..* If a conversion percentage is assumed and a Logistic Classification model was fit on the data an accuracy of 85% is observed.
..* Gives indication that if the content type, size was known and adding varied weights on the content files can give us prediction for possible conversion.

## Some Insights
..* The distribution of the view time across the industries varies from a mean of 1 minute to 4 minutes.
..* The maximum views happened during the weekdays across all the industries except one which had an unusual pattern of the views peaking on Thursdays.
..* Study in-depth why this pattern exists and whether it increases view rate.
..* Future data collection should include more content and conversion information.

## Company's Response
..* Very excited to see the data visualization of user activity for all customers compared to each other.
..* This analysis will help them show their customers what can be done with the data.
..* Could potentially convince the customers to release more data for more predictive analyses in future.  
