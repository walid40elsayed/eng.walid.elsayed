-- Data Exploration
------------------------
------------------------

-- Check Distinct Values
------------------------

-- check the total count for all customers amd calculate the percentages of each Gender
-- check percentages for all gender 

SELECT Gender, Count(Gender) as TotalCount,
Count(Gender) * 100.0 / (Select Count(*) from stg_Churn)  as Percentage
from stg_Churn
Group by Gender

-- check the types of subscribtions contract and total of those contracts

SELECT Contract, Count(Contract) as TotalCount,
Count(Contract) * 100.0 / (Select Count(*) from stg_Churn)  as Percentage
from stg_Churn
Group by Contract

-- check status of each customer 
SELECT Customer_Status, Count(Customer_Status) as TotalCount, Sum(Total_Revenue) as TotalRev,
Sum(Total_Revenue) / (Select sum(Total_Revenue) from stg_Churn) * 100  as RevPercentage
from stg_Churn
Group by Customer_Status

-- check the percentage of each state 
SELECT State, Count(State) as TotalCount,
Count(State) * 1.0 / (Select Count(*) from stg_Churn)  as Percentage
from stg_Churn
Group by State
Order by Percentage desc

------------------------------------------------------------------------------------------
 -- Check Nulls

 -- 1- check nulls in each coloumn then if there is null add 1 and if ther id no add 0 
 -- 2- then create new column finished by null_count for each of coloumns
 -- 3- that new coloumn will contain the count of ech nulls vslues in each coloumn
 SELECT 
    SUM(CASE WHEN Customer_ID IS NULL THEN 1 ELSE 0 END) AS Customer_ID_Null_Count,
    SUM(CASE WHEN Gender IS NULL THEN 1 ELSE 0 END) AS Gender_Null_Count,
    SUM(CASE WHEN Age IS NULL THEN 1 ELSE 0 END) AS Age_Null_Count,
    SUM(CASE WHEN Married IS NULL THEN 1 ELSE 0 END) AS Married_Null_Count,
    SUM(CASE WHEN State IS NULL THEN 1 ELSE 0 END) AS State_Null_Count,
    SUM(CASE WHEN Number_of_Referrals IS NULL THEN 1 ELSE 0 END) AS Number_of_Referrals_Null_Count,
    SUM(CASE WHEN Tenure_in_Months IS NULL THEN 1 ELSE 0 END) AS Tenure_in_Months_Null_Count,
    SUM(CASE WHEN Value_Deal IS NULL THEN 1 ELSE 0 END) AS Value_Deal_Null_Count,
    SUM(CASE WHEN Phone_Service IS NULL THEN 1 ELSE 0 END) AS Phone_Service_Null_Count,
    SUM(CASE WHEN Multiple_Lines IS NULL THEN 1 ELSE 0 END) AS Multiple_Lines_Null_Count,
    SUM(CASE WHEN Internet_Service IS NULL THEN 1 ELSE 0 END) AS Internet_Service_Null_Count,
    SUM(CASE WHEN Internet_Type IS NULL THEN 1 ELSE 0 END) AS Internet_Type_Null_Count,
    SUM(CASE WHEN Online_Security IS NULL THEN 1 ELSE 0 END) AS Online_Security_Null_Count,
    SUM(CASE WHEN Online_Backup IS NULL THEN 1 ELSE 0 END) AS Online_Backup_Null_Count,
    SUM(CASE WHEN Device_Protection_Plan IS NULL THEN 1 ELSE 0 END) AS Device_Protection_Plan_Null_Count,
    SUM(CASE WHEN Premium_Support IS NULL THEN 1 ELSE 0 END) AS Premium_Support_Null_Count,
    SUM(CASE WHEN Streaming_TV IS NULL THEN 1 ELSE 0 END) AS Streaming_TV_Null_Count,
    SUM(CASE WHEN Streaming_Movies IS NULL THEN 1 ELSE 0 END) AS Streaming_Movies_Null_Count,
    SUM(CASE WHEN Streaming_Music IS NULL THEN 1 ELSE 0 END) AS Streaming_Music_Null_Count,
    SUM(CASE WHEN Unlimited_Data IS NULL THEN 1 ELSE 0 END) AS Unlimited_Data_Null_Count,
    SUM(CASE WHEN Contract IS NULL THEN 1 ELSE 0 END) AS Contract_Null_Count,
    SUM(CASE WHEN Paperless_Billing IS NULL THEN 1 ELSE 0 END) AS Paperless_Billing_Null_Count,
    SUM(CASE WHEN Payment_Method IS NULL THEN 1 ELSE 0 END) AS Payment_Method_Null_Count,
    SUM(CASE WHEN Monthly_Charge IS NULL THEN 1 ELSE 0 END) AS Monthly_Charge_Null_Count,
    SUM(CASE WHEN Total_Charges IS NULL THEN 1 ELSE 0 END) AS Total_Charges_Null_Count,
    SUM(CASE WHEN Total_Refunds IS NULL THEN 1 ELSE 0 END) AS Total_Refunds_Null_Count,
    SUM(CASE WHEN Total_Extra_Data_Charges IS NULL THEN 1 ELSE 0 END) AS Total_Extra_Data_Charges_Null_Count,
    SUM(CASE WHEN Total_Long_Distance_Charges IS NULL THEN 1 ELSE 0 END) AS Total_Long_Distance_Charges_Null_Count,
    SUM(CASE WHEN Total_Revenue IS NULL THEN 1 ELSE 0 END) AS Total_Revenue_Null_Count,
    SUM(CASE WHEN Customer_Status IS NULL THEN 1 ELSE 0 END) AS Customer_Status_Null_Count,
    SUM(CASE WHEN Churn_Category IS NULL THEN 1 ELSE 0 END) AS Churn_Category_Null_Count,
    SUM(CASE WHEN Churn_Reason IS NULL THEN 1 ELSE 0 END) AS Churn_Reason_Null_Count
FROM stg_Churn;

------------------------------------------------------------------------------------------------
-- Removing Nulls

-- Create new table for clean data to start 

SELECT 
    Customer_ID, -- no nulls
    Gender,  -- no nulls
    Age,  -- no nulls
    Married,  -- no nulls
    State,  -- no nulls
    Number_of_Referrals,                                                           -- no nulls
    Tenure_in_Months,                                                              -- no nulls
    ISNULL(Value_Deal, 'None') AS Value_Deal,                                      -- contain nulls
    Phone_Service,                                                                 -- no nulls
    ISNULL(Multiple_Lines, 'No') As Multiple_Lines,                                -- contain nulls
    Internet_Service,                                                              -- no nulls
    ISNULL(Internet_Type, 'None') AS Internet_Type,                                -- contain nulls
    ISNULL(Online_Security, 'No') AS Online_Security,                              -- contain nulls
    ISNULL(Online_Backup, 'No') AS Online_Backup,                                  -- contain nulls
    ISNULL(Device_Protection_Plan, 'No') AS Device_Protection_Plan,                -- contain nulls
    ISNULL(Premium_Support, 'No') AS Premium_Support,                              -- contain nulls
    ISNULL(Streaming_TV, 'No') AS Streaming_TV,                                    -- contain nulls
    ISNULL(Streaming_Movies, 'No') AS Streaming_Movies,                            -- contain nulls
    ISNULL(Streaming_Music, 'No') AS Streaming_Music,                              -- contain nulls
    ISNULL(Unlimited_Data, 'No') AS Unlimited_Data,                                -- contain nulls
    Contract,                                                                      -- no nulls
    Paperless_Billing,                                                             -- no nulls
    Payment_Method,                                                                -- no nulls
    Monthly_Charge,                                                                -- no nulls
    Total_Charges,                                                                 -- no nulls
    Total_Refunds,                                                                 -- no nulls
    Total_Extra_Data_Charges,                                                      -- no nulls
    Total_Long_Distance_Charges,                                                   -- no nulls
    Total_Revenue,                                                                 -- no nulls
    Customer_Status,                                                               -- no nulls
    ISNULL(Churn_Category, 'Others') AS Churn_Category,                            -- contain nulls
    ISNULL(Churn_Reason , 'Others') AS Churn_Reason                                -- contain nulls

INTO [db_Churn].[dbo].[prod_Churn]
FROM [db_Churn].[dbo].[stg_Churn];

------------------------------------------------------------------------------

-- Create View for Power BI

Create View vw_ChurnData as
	select * from prod_Churn where Customer_Status In ('Churned', 'Stayed')


Create View vw_JoinData as
	select * from prod_Churn where Customer_Status = 'Joined'

