
## <mark style="background: #ADCCFFA6;">Biostatistics</mark>

<mark style="background: #FFB8EBA6;">Biostatistics</mark> is the theory and methodology for the acquisition and use of quantitative evidence in biomedical research. Biostatisticians develop innovative designs and analytic methods targeted at increasing available information, improving the relevance and validity of statistical analyses, making best use of available information and communicating relevant uncertainties.

Examples:

### <mark style="background: #ABF7F7A6;">HRT</mark>

A large clinical trial (the Women's Health Initiative) published results in 2002 that contradicted prior evidence on the efficacy of hormone replacement therapy for post menopausal women and suggested a negative impact of HRT for several key health outcomes. **Based on a statistically based protocol, the study was stopped early due to an excess number of negative events**.

### <mark style="background: #ABF7F7A6;">ECMO (Extracorporeal membrane oxygenation treatment)</mark>

In 1985 a group at a major neonatal intensive care center published the results of a trial comparing a standard treatment and a promising ECMO for newborn infants with sever respiratory failure. **Ethical considerations lead to a statistical randomization scheme whereby one infant received the control therapy, thereby opening the study to sample-size based criticisms**. (Only one infant received the control therapy)

### <mark style="background: #ABF7F7A6;">Summary</mark>

* These examples illustrate the central role that biostatistics plays in public health and the importance of performing design, analysis and interpretation of statistical data correctly.
* At the John Hopkins Bloomberg School of Public Health, the prevailing philosophy or conducting biostatistics includes:
	* A tight coupling of the statistical methods with the ethical and scientific goals.
	* Emphasizing scientific interpretation of statistical evidence to impact policy.
	* Acknowledging and assumptions and evaluating the robustness of conclusions to them.



## <mark style="background: #ADCCFFA6;">Experiments</mark>

Consider the outcome of an **experiment** such as:
* a collection of measurements from a sampled population
* measurements from a laboratory experiment
* the result of a clinical trial
* the result from a simulated (computer) experiment
* values from hospital records sampled retrospectively (retrospectively sampling, useful when studying a phenomenon)
* ...


## <mark style="background: #ADCCFFA6;">Set Notation</mark>

* The **<mark style="background: #FF5582A6;">sample space</mark>**, $\Omega$, is the collection of possible outcomes of an experiment.
	Example: die roll $\Omega$ = {1,2,3,4,5,6}
* An **<mark style="background: #FF5582A6;">event</mark>**, say E, is a subset of $\Omega$
	Example: Die roll is even E = {2,4,6}
* An **<mark style="background: #FF5582A6;">elementary</mark>** or **<mark style="background: #FF5582A6;">simple</mark>** event is a particular result of an experiment
	Example: die roll is four, $\omega$ = 4
* $\emptyset$ is called the **<mark style="background: #FF5582A6;">null event</mark>** or **<mark style="background: #FF5582A6;">empty set</mark>**

Normal set operations have particular interpretations in this setting:

1) $\omega \in E$ implies that E occurs when $\omega$ occurs
2) $\omega \notin E$ implies that E does not occur when $\omega$ occurs
3) $E \subset F$ implies that the occurrence of E implies the occurrence of F
4) $E \cap F$ implies the event that both E and F occur
5) $E \cup F$ implies the event that at least one of E or F occur
6) $E \cap F = \emptyset$ means that E and F are **<mark style="background: #FF5582A6;">mutually exclusive</mark>**, or cannot both occur
7) $E^{c}$ or $\bar{E}$  is the event that E does not occur

* DeMorgan's Laws

	$(A \cap B)^{c} = A^{c} \cup B^{c}$
	$(A \cup B)^{c} = A^{c} \cap B^{c}$
	
	Example: If an alligator or a turtle you are not $(A \cup B)^{c}$ then you are not an alligator and you are also not a turtle $(A \cap B)^{c}$
	
	Example: If your car is not both hybrid and diesel $(A \cap B)^{c}$ then your car is either not hybrid or not diesel $(A^c \cup B^c)$

* $(A^c)^c = A$
* $(A \cup B) \cap C = (A \cap C) \cup (B \cap C)$


## <mark style="background: #ADCCFFA6;">Probability</mark>

* Useful strategy used in much of science:
	For a given experiment
		* attribute all that is known or theorized to a systematic model (mathematical function)
		* attribute everything else to randomness, even if the process under study is not known not the be "random" in any sense of the word
		* Use probability to quantify the uncertainty in your conclusions
		* Evaluate the sensitivity of your conclusions to the assumptions of your model

Questions to keep in mind for probability!

* What is being modeled as random?
* Where does this attributed randomness arise from?
* Where did the systematic model components arise from?
* How did observational units come to be in the study and is there importance to the missing data points?
* Do the results generalize beyond the study in question?
* Were important variables unaccounted for in the model?
* How drastically would inferences change depending on the answers to the previous questions?