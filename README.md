  **This project was to predict diabetese using ML with the help of BRFSS 2022 data set And By Evaluating 2 classification models on our dataset , building that model(i.e. better performing on our dataset) from scratch.**
 - The Behavioral Risk Factor Surveillance System (BRFSS) is an initiative taken by CDC to do telephone surveys that collect state data about U.S .
 - It is designed to collect state-specific data on various health-related behaviors among adults, including risk factors for chronic diseases, injuries, and preventive health practices.
 - Based on the suveys data of year 2022 we try to find out factors affecting diabetese and created a model to predict diabetese



 **STEPS INVOLVED:-**
 
	 • Downloaded SAS data provided by CDC
	 • Converted it into csv(i.e. converted for ml usable format) for further usage
[link to zip files that have been downloaded from CDC and converted into csv](https://github.com/Dipesh-Chaudhary/MLProjectDiabetesPredictionUsingBRFSS2022/tree/main/1%20ACCESSING%20SAS%20DATAS%20AND%20CONVERTING%20INTO%20CSV%20USING%20SAS%20STUDIO)



  
	 • Data collection and cleaning was done
[Notebook for above steps](https://github.com/Dipesh-Chaudhary/MLProjectDiabetesPredictionUsingBRFSS2022/blob/main/2%20Files%20of%20notebooks%20for%20different%20steps/1%20Data%20Collection%20and%20cleaning/22DataCollectionAndCleaning.ipynb)



  	 • Preprocessing and EDA was done
    
[Notebook for above steps](https://github.com/Dipesh-Chaudhary/MLProjectDiabetesPredictionUsingBRFSS2022/blob/main/2%20Files%20of%20notebooks%20for%20different%20steps/2%20Preprocessing%20With%20EDA/22PreprocessingAndEDA.ipynb)


    
	 • Comparison between k-nn and naive baye's model was done 
  [Notebook for above steps](https://github.com/Dipesh-Chaudhary/MLProjectDiabetesPredictionUsingBRFSS2022/blob/main/2%20Files%20of%20notebooks%20for%20different%20steps/3%20Model%20Selection/22Modelselection.ipynb)


  
  	• Best performing model between them (k-nn model) on our dataset was built from scratch
   	• Validation and Evaluation was done of our newly built model from scratch on our preprocessed dataset
[Notebook for above steps](https://github.com/Dipesh-Chaudhary/MLProjectDiabetesPredictionUsingBRFSS2022/blob/main/2%20Files%20of%20notebooks%20for%20different%20steps/4%20Model%20Building/22knnFromScratch.ipynb)
	

  

	 • Web app was made using streamlit 
[python code](https://github.com/Dipesh-Chaudhary/MLProjectDiabetesPredictionUsingBRFSS2022/blob/main/2%20Files%20of%20notebooks%20for%20different%20steps/5%20web%20app/DiabetesWebApp.py)

	 • [Deployment was done through Streamlit cloud](https://predict-diabetese.streamlit.app/)
  [Deployed model](https://predict-diabetese.streamlit.app/)



