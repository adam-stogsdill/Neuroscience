Tags: #WorkResearch

In this work, we are trying to understand and better design metrics focused on better knowing our ensemble’s general performance.

## Why do the ones we have fail?

I think there are a few initial reasons as to why our metrics fail for each model.
1. Lack of data! → The lack of data is going to create a difficult idea for understanding the overall generalizability of the model which is what metrics are supposed to do but this can only go so far.
2. Lack of model stability → A side effect of the lack of data means that when we perform metrics on data, we can add or remove a single file that may be within the boundary of easily and not easily classified data points and can make the model’s performance jump around.
3. Simple metrics → These metrics work for simple problems but we generally want to understand more about the model’s behavior. Metrics such as Average, STD, Precision, Recall, and F1-scores, are only gonna tell us so much.

## What do I believe we can do?

I think there is a few general paths that we can go. However, I will preface this with the idea that we need to understand more of our models first!
* Take a model first approach, understand the embedding space created by the CNN layers of each model. Are there clusters? Are there meaningful connections between bits of data?
* Take a data first approach, understand some deeper associations within the data and see the general performance on these associations!
As you can see both of the approaches are theoretical and research heavy in their own ways. I think that the model first approach is the least difficult road to first travel. Understanding model behavior is always great! However, I believe that a data first approach is going to help us understand our data and make models better generalized based off our observations by feeding better initial features (of course I say “Initial” because the NN will use transformations on those features to make the final process of classification)

# Model First Approach

In the Model First Approach, I propose using masking and artificial noise to get a general sense of the models and their behavior on the data. Doing this will require a few different pathways which I will try and explore here in the documentation. In this portion of the documentation, I want to show methods and examine methods that will explore, or eventually depend on, to further our understanding of the model’s behavior in different data inputs. Using masking/noise as the basis of the methodology here, we can avoid the need for extra data while also manipulating the data to create a wider sense of the latent space that is created within the CNN’s convolutional layers.

## Zero-Valued Masks

Three-dimensional zero-valued masks will essentially nullify targeted areas of data as if there was no noise in the time/frequency range desired. This method is easily understood in the case where the mask M with the size (1,1,1). The process is as follows:

1. Load Trained Model
2. Create a zero-valued mask M of size (1,1,1)
3. Apply that mask at each pixel of the image, recording the change in output from the model when observing the image
4. Look at the “heatmap” that is generated from this to understand what pixel ranges are important to the classification problem.

Though this method is simple, it fails to understand that pixels are more likely going to have approximate pixels affect the outcome of the classification value. This is where the process becomes difficult! I need a way to model how the models affect the performance of other when they are masked out. This case would mean we would be able to generalize to a mask size of (1,N,M). My initial thought is to use something similar to a covariance matrix, where we mark the changes that occur when a certain group of pixel are masked, but the complexity of that matrix will become very large. For now I have a simple solution for this! Frequency-based masking.

### Frequency-based Masking