% Consulting Soft Skills
% Chris Shurtleff
% August 22, 2022

# What is a Data Lake?

## Data Lake:

![Trash under lake Erie](slide_images/lake_trash_erie.jpeg)

- Like a regular lake, filled with all sorts of interesting garbage.
- If you need something, get a magnet! (High-effort retrieval)

::: notes
- In most comparisons it's more like the _water_ is the data, but this is funnier.
- It's going to be easier to tell benefits when compared with a Data Warehouse
- Useful for anything that doesn't have a standard structure
:::

## Data Lake vs Data Warehouse

- Data Warehouse has _structured_ data
- Data Lake has _unstructured_ data
- Structured data requires knowing _precisely_ how to describe what you want to keep in advance
- Unstructured lets you keep some data that you _might_ want to use later
- Semi-structured data lets you apply _some_ structure to otherwise unstructured data

::: notes
- Unstructured examples:
    Video, audio, image files, log files, sensor files
- Structured examples:
    Relational data (excel, SQL)
:::

# Serverless architecture

## What is serverless?

![Scooters in Columbus](slide_images/Columbus_electric_scooters.jpg)

- Using somebody else's computers
- Like sharing these scooters, but for computers!
- Allows a third party to absorb and distribute costs among many clients

::: notes
- Scooter share services also tend to use serverless architecture.
:::

## Serverless Pros

::: incremental
- Lower overall costs
- Replaces fixed costs with variable costs
- Complicated compliance and security issues are someone else's problem!
- Extremely easy to ensure continual access to data
- Set up is easier
- Changing things is easier
:::

::: notes
- Pay only what you use!
- Physical security is hard, let someone else do it
- Compliance can be a headache, if it's not what you are making money from you should probably let someone else deal with that hassle.
:::

## Serverless Cons

::: incremental
- Relatively easy to accidentally pay for _significantly_ more than you need.
- Somebody else _owns_ and _secures_ the physical computers
- Can be more expensive than not serverless alternatives
:::

::: notes
- It _can be_ significantly more secure, because security is hard and part of it is someone else's problem now
- It _cannot be_ entirely secure, because somebody else has physical access to the computers
- Realistically it's a complicated tradeoff that is _usually_ more secure, _usually_ cheaper, and _usually_ easier to use.
:::

## ETL Pipeline

::: notes
TODO: Make a diagram of the ETL, then add notes
:::

# Modern MLOps

## Machine Learning
- Set of algorithms that can be broadly applied across different sets of data
- Mostly applied for _prediction_ and _classification_
- Examples:
    - Given sensor data, what is the operator of this machine _doing_ (classification)
    - Given the state of a chess game, which move will lead to an ultimate victory (prediction)

## How to make an ML model
Generic Supervised approach:

- Build set of _features_ from input data
- Determine the _label_ of each set of _features_
- _Train_ the features, finding the right _weights_ that lead from input to label
- _Validate_ the weights and algorithm writ large
- _Test_ the weights to determine _accuracy_ and _discrimination_

::: notes
_features_: The input data. The sensor data of the machine, the current state of play of chessboard
_label_: What a set of _features_ should tell you. The intention of the operator, the value of a potential future state of the chessboard
_Train_: A generic term for applying an error function to evaluate whether the _label_ matches the _features_. Finds the _weights_ (usually a _tensor_) that can evaluate the _features_ into the correct _label_
_Validate_: Most ML models will have hyperparameters, and _which_ ML model you are using can be thought of as another hyperparameter. Finding out which hyperparameter gives the best results for your particular problem is what this step is for.
_Test_: At the end of the day, you need to check for whether when you apply the model to new data, it still provides useful or correct predictions/classifications. This step requires you to reserve some sample of the original, labelled data and check whether your new set of _weights_ still applies to them.
_accuracy_: If we decided that the input was 'A' did the algorithm output 'A'?
_discrimination_: What is the exact tradeoff between when our algorithm was wrong and when it was right?
:::

## Applied ML Models (MLOps)
Automate the last slide!!!

- Automatic data (or ETL) pipelines to generate _features_ from input data
- Apply the ML model to the new _features_, creating a set of _labels_
- Use the _labels_ as you see fit!
- *IMPORTANT* Validate the algorithm over time, to make sure the relationship doesn't shift!

## MLOps in practice
- .yaml, .json, and .py files to define the ETL _infrastructure_
- .yaml, .json, and .py files to define the ETL _pipelines_ for feature generation from input data
- .yaml, .json, and .py files to define the compute necessary for finding the correct _weights_
- .yaml, .json, and .py files to define the compute necessary for applying _weights_ to new data
- .yaml, .json, and .py files to define where the _labels_ and _features_
- Unit tests for checking various steps for issues
- Logs for troubleshooting problems
- Validation: Make sure the relationship between _features_ and _labels_ doesn't shift over time!

::: notes

:::
