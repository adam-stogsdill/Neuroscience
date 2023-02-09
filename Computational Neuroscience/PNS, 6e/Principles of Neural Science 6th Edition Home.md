
```dataview
TABLE length(filter(file.tasks, (t) => t.completed)) as "Completed", length(filter(file.tasks, (t) => !t.completed)) AS "Uncompleted", length(filter(file.tasks, (t) => t.completed))/ length(filter(file.tasks, (t) => !t.completed)) * 100 as "Percent Complete" WHERE file.tasks AND length(file.tasks) > 0 AND length(filter(file.tasks, (t) => !t.completed)) > 0
```

## Part I - Overall Perspective

### 1 The Brain and Behavior
- [x] Two Opposing Views Have Been Advanced on the Relationship Between Brain and Behavior ✅ 2023-01-24
- [x] The Brain Has Distinct Functional Regions ✅ 2023-01-24
- [x] The First Strong Evidence for Localization of Cognitive Abilities Came From Studies of Language Disorders ✅ 2023-01-24
- [x] Mental Processes are the Product of Interactions Between Elementary Processing Units in the Brain ✅ 2023-01-24

### 2 Genes and Behavior
- [x] An Understanding of Molecular Genetics and Heritability Is Essential to the Study of Human Behavior ✅ 2023-01-24
- [x] The Understanding of the Structure and Function of the Genome is Evolving ✅ 2023-01-25
	- [x] Genes Are Arranged on Chromosomes ✅ 2023-01-25
- [x] The Relationship Between Genotype and Phenotype Is Often Complex ✅ 2023-01-25
- [x] Genes are Conserved Through Evolution ✅ 2023-01-26
- [x] Genetic Regulation of Behavior Can Be Studied in Animal Models ✅ 2023-01-27
	- [x] A Transcriptional Oscillator Regulates Circadian Rhythm in Flied, Mice, and Humans ✅ 2023-02-05
	- [x] Natural Variation in a Protein Kinase Regulates Activity in Flied and Honeybees ✅ 2023-02-06
	- [x] Neuropeptide Receptors Regulate the Social Behaviors of Several Species ✅ 2023-02-07
- [x] Studies of Human Genetic Syndromes Have Provided Initial Insights Into the Underpinnings of Social Behavior ✅ 2023-02-07
	- [x] Brain Disorders in Humans Result From Interactions Between Genes and the Environment ✅ 2023-02-07
	- [x] Rare Neurodevelopmental Syndromes Provide Insights Into the Biology of Social Behavior, Perception, and Cognition ✅ 2023-02-07
- [x] Psychiatric Disorders Involve Multigenic Traits ✅ 2023-02-07
	- [x] Advances in Autism Spectrum Disorder Genetics Highlight the Role of Rare and De Novo Mutations in Neurodevelopmental Disorders ✅ 2023-02-07
	- [x] Identification of Genes for Schizophrenia Highlights the Interplay of Rare and Common Risk Variants ✅ 2023-02-07
- [x] Perspectives on The Genetic Bases of Neuropsychiatric Disorders ✅ 2023-02-07

### 3 Nerve Cells, Neural Circuitry, and Behavior
- [x] The Nervous System Has Two Classes of Cells ✅ 2023-02-08
	- [ ] Nerve Cells Are the Signaling Units of the Nervous System
	- [ ] Glial Cells Support Nerve Cells
- [ ] Each Nerve Cell Is Part of a Circuit That Mediates Specific Behaviors
- [ ] Signaling Is Organized in the Same Way in All Nerve Cells
	- [ ] The Input Component Produces Graded Local Signals
	- [ ] The Trigger Zone Makes the Decision to Generate an Action Potential
	- [ ] The Output Component Releases Neurotransmitter
	- [ ] The Transformation of the Neural Signal From Sensory to Motor Is Illustrated by the Stretch-Reflex Pathway
- [ ] Nerve Cells Differ Most at the Molecular Level
- [ ] The Reflex Circuit Is a Starting Point for Understanding the Neural Architecture of Behavior
- [ ] Neural Circuits Can Be Modified by Experience

### 4 The Neuroanatomical Bases by Which Neural Circuits Mediate Behavior
- [ ] Local Circuits Carry Out Specific Neural Computations That Are Coordinated to Mediate Complex Behaviors
- [ ] Sensory Information Circuits Are Illustrated in the Somatosensory System
	- [ ] Somatosensory Information From the Trunk and Limbs Is Conveyed to the Spinal Cord 
	- [ ] The Primary Sensory Neurons of the Trunk and Limbs Are Clustered in the Dorsal Root Ganglia
	- [ ] The Terminals of Central Axons of Dorsal Root Ganglion Neurons in the Spinal Cord Produce a Map of the Body Surface
	- [ ] Each Somatic Submodality Is Processed in a Distinct Subsystem From the Periphery to the Brain
- [ ] The Thalamus Is an Essential Link Between Sensory Receptors and the Cerebral Cortex
- [ ] Sensory Information Processing Culminates in the Cerebral Cortex
- [ ] Voluntary Movement Is Mediated by Direct Connections Between the Cortex and Spinal Cord
- [ ] Modulatory Systems in the Brain Influence Motivation, Emotion, and Memory
- [ ] The Peripheral Nervous System Is Anatomically Distinct From the Central Nervous System
- [ ] Memory Is a Complex Behavior Mediated by Structures Distinct From Those That Carry Out Sensation or Movement
	- [ ] The Hippocampal System Is Interconnected With the Highest-Level Polysensory Cortical Regions
	- [ ] The Hippocampal Formation Comprises Several Different but Highly Integrated Circuits
	- [ ] The Hippocampal Formation Is Made Up Mainly of Unidirectional Connections

### 5 The Computational Bases of Neural Circuits That Mediate Behavior
- [ ] Neural Firing Patterns Provide a Code for Information
	- [ ] Sensory Information Is Encoded by Neural Activity
	- [ ] Information Can Be Decoded From Neural Activity
	- [ ] Hippocampal Spatial Cognitive Maps Can Be Decoded to Infer Location
- [ ] Neural Circuit Motifs Provide a Basic Logic for Information Processing 
	- [ ] Visual Processing and Object Recognition Depend on Hierarchy of Feed-Forward Representations
	- [ ] Diverse Neuronal Representations in the Cerebellum Provide a Basis for Learning
	- [ ] Recurrent Circuitry Underlies Sustained Activity and Integration
- [ ] Learning and Memory Depend on Synaptic Plasticity
	- [ ] Dominant Patterns of Synaptic Input Can be Identified by Hebbian Plasticity
	- [ ] Synaptic Plasticity in the Cerebellum Plays a Key Role in Motor Learning`

### 6 Imaging and Behavior
- [ ] Functional MRI Experiments Measure Neurovascular Activity
	- [ ] fMRI Depends on the Physics of Magnetic Resonance
	- [ ] fMRI Depends on the Biology of Neurovascular Coupling
- [ ] Functional MRI Data Can Be Analyzed in Several Ways
	- [ ] fMRI Data First Need to Be Prepared for Analysis by Following Preprocessing Steps
	- [ ] fMRI Can Be Used to Localize Cognitive Functions to Specific Brain Regions
	- [ ] fMRI Can Be Used to Decode What Information Is Represented in the Brain
	- [ ] fMRI Can Be Used to Measure Correlated Activity Across Brain Networks
- [ ] Functional MRI Studies Have Led to Fundamental Insights
	- [ ] fMRI Studies in Humans Have Inspired Neurophysiological Studies in Animals
	- [ ] fMRI Studies Have Challenged Theories From Cognitive Psychology and Systems Neuroscience
	- [ ] fMRI Studies Have Tested Predictions From Animal Studies and Computational Models
- [ ] Functional MRI Studies Require Careful Interpretation
- [ ] Future Progress Depends on Technological and Conceptual Advances

## Part II - Cell and Molecular Biology of Cells of the Nervous System

### 7 The Cells of the Nervous System
- [ ] Neurons and Glia Share Many Structural and Molecular Characteristics
- [ ] The Cytoskeleton Determines Cell Shape
- [ ] Protein Particles and Organelles Are Actively Transported Along the Axon and Dendrites
	- [ ] Fast Axonal Transport Carries Membranous Organelles
	- [ ] Slow Axonal Transport Carries Cytosolic Proteins and Elements of the Cytoskeleton
- [ ] Proteins Are Made in Neurons as in Other Secretory Cells
	- [ ] Secretory and Membrane Proteins Are Synthesized and Modified in the Endoplasmic Reticulum
	- [ ] Secretory Proteins Are Modified in the Golgi Complex
- [ ] Surface Membrane and Extracellular Substances Are Recycled in the Cell
- [ ] Glial Cells Play Diverse Roles in Neural Function
	- [ ] Glia Form the Insulating Sheaths for Axons
	- [ ] Astrocytes Support Synaptic Signaling
	- [ ] Microglia Have Diverse Functions in Health and Disease
- [ ] Choroid Plexus and Ependymal Cells Produce Cerebrospinal Fluid

## 8 Ion Channels
- [ ] Ion Channels Are Proteins That Span the Cell Membrane
- [ ] Ion Channels in All Cells Share Several Functional Characteristics
	- [ ] Currents Through Single Ion Channels Can Be Recorded
	- [ ] The Flux of Ions Through a Channel Differs From Diffusion in Free Solution
	- [ ] The Opening and Closing of a Channel Involve Conformational Changes
- [ ] The Structure of Ion Channels Is Inferred From Biophysical, Biochemical, and Molecular Biological Studies
	- [ ] Ion Channels Can Be Grouped Into Gene Families
	- [ ] X-Ray Crystallographic Analysis of Potassium Channel Structure Provides Insight Into Mechanisms of Channel Permeability and Selectivity
	- [ ] X-Ray Crystallographic Analysis of Voltage-Gated Potassium Channel Structures Provides Insight Into Mechanisms of Channel Gating
	- [ ] The Structural Basis of the Selective Permeability of Chloride Channels Reveals a Close Relation Between Channels and Transporters

### 9 Membrane Potential and the Passive Electrical Properties of the Neuron
- [ ] The Resting Membrane Potential Results From the Separation of Charge Across the Cell Membrane
- [ ] The Resting Membrane Potential Is Determined by Nongated and Gated Ion Channels
	- [ ] Open Channels in Glial Cells Are Permeable to Potassium Only
	- [ ] Open Channels in Resting Nerve Cells Are Permeable to Three Ion Species
	- [ ] The Electrochemical Gradients of Sodium, Potassium, and Calcium Are Established by Active Transport of the Ions
	- [ ] Chloride Ions Are Also Actively Transported
- [ ] The Balance of Ion Fluxes in the Resting Membrane Is Abolished During the Action Potential
- [ ] The Contributions of Different Ions to the Resting Membrane Potential Can Be Quantified by the Goldman Equation
- [ ] The Functional Properties of the Neuron Can Be Represented as an Electrical Equivalent Circuit
- [ ] The Passive Electrical Properties of the Neuron Affect Electrical Signaling
	- [ ] Membrane Capacitance Slows the Time Course of Electrical Signals
	- [ ] Membrane and Cytoplasmic Resistance Affect the Efficiency of Signal Conduction
	- [ ] Large Axons Are More Easily Excited Than Small Axons
	- [ ] Passive Membrane Properties and Axon Diameter Affect the Velocity of Action Potential Propagation

### 10 Propagated Signaling: The Action Potential
- [ ] The Action Potential Is Generated by the Flow of Ions Through Voltage-Gated Channels
	- [ ] Sodium and Potassium Currents Through Voltage-Gated Channels Are Recorded With the Voltage Clamp
	- [ ] Voltage-Gated Sodium and Potassium Conductances Are Calculated From Their Currents
	- [ ] The Action Potential Can Be Reconstructed From the Properties of Sodium and Potassium Channels
- [ ] The Mechanisms of Voltage Gating Have Been Inferred From Electrophysiological Measurements
- [ ] Voltage-Gated Sodium Channels Select for Sodium on the Basis of Size, Charge, and Energy of Hydration of the Ion
- [ ] Individual Neurons Have a Rich Variety of Voltage-Gated Channels That Expand Their Signaling Capabilities
	- [ ] The Diversity of Voltage-Gated Channel Types Is Generated by Several Genetic Mechanisms
	- [ ] Voltage-Gated Sodium Channels
	- [ ] Voltage-Gated Calcium Channels
	- [ ] Voltage-Gated Potassium Channels
	- [ ] Voltage-Gated Hyperpolarization-Activated Cyclic Nucleotide-Gated Channels
- [ ] Gating of Ion Channels Can Be Controlled by Cytoplasmic Calcium
- [ ] Excitability Properties Vary Between Types of Neurons
- [ ] Excitability Properties Vary Between Regions of the Neuron
- [ ] Neural Excitability Is Plastic

## Part III - Synaptic Transmission

### 11 Overview of Synaptic Transmission
- [ ] Synapses Are Predominantly Electrical or Chemical
- [ ] Electrical Synapses Provide Rapid Signal Transmission
	- [ ] Cells at an Electrical Synapse Are Connected by Gap-Junction Channels
	- [ ] Electrical Transmission Allows Rapid and Synchronous Firing of Interconnected Cells
	- [ ] Gap Junctions Have a Role in Glial Functions and Disease
- [ ] Chemical Synapses Can Amplify Signals
	- [ ] The Action of a Neurotransmitter Depends on the Properties of the Postsynaptic Receptor
	- [ ] Activation of Postsynaptic Receptors Gates Ion Channels Either Directly or Indirectly
- [ ] Electrical and Chemical Synapses Can Coexist and Interact

## 12 Directly Gated Transmission
- [ ] The Neuromuscular Junction Has Specialized Presynaptic and Postsynaptic Structures
	- [ ] The Postsynaptic Potential Results From a Local Change in Membrane Permeability
	- [ ] The Neurotransmitter Acetylcholine Is Released in Discrete Packets
- [ ] Individual Acetylcholine Receptor-Channels Conduct All-or-None Currents
	- [ ] The Ion Channel at the End-Plate Is Permeable to Both Sodium and Potassium Ions
	- [ ] Four Factors Determine the End-Plate Current
- [ ] The Acetylcholine Receptor-Channels Have Distinct Properties That Distinguish Them From the Voltage-Gated Channels That Generate the Muscle Action Potential
	- [ ] Transmitter Binding Produces a Series of State Changes in the Acetylcholine Receptor-Channel
	- [ ] The Low-Resolution Structure of the Acetylcholine Receptor is Revealed by Molecular and Biophysical Studies
	- [ ] The High-Resolution Structure of the Acetylcholine Receptor-Channel Is Revealed by X-Ray Crystal Studies
- [ ] Postscript: The End-Plate Current Can Be Calculated From an Equivalent Circuit

## 13 Synaptic Integration in the Central Nervous System
- [ ] Central Neurons Receive Excitatory and Inhibitory Inputs
- [ ] Excitatory and Inhibitory Synapses Have Distinctive Ultrastructures and Target Different Neuronal Regions
- [ ] Excitatory Synaptic Transmission Is Mediated by Ionotropic Glutamate Receptor-Channels Permeable to Cations
	- [ ] The Ionotropic Glutamate Receptors Are Encoded by a Large Gene Family
	- [ ] Glutamate Receptors Are Constructed From a Set of Structural Modules
	- [ ] NMDA and AMPA Receptors are Organized by a Network of Proteins at the Postsynaptic Density
	- [ ] NMDA Receptors Have Unique Biophysical and Pharmacological Properties
	- [ ] The Properties of the NMDA Receptor Underlie Long-term Synaptic Plasticity
	- [ ] NMDA Receptors Contribute to Neuropsychiatric Disease
- [ ] Fast Inhibitory Synaptic Actions Are Mediated by Ionotropic GABA and Glycine Receptor-Channels Permeable to Chloride
- [ ] Ionotropic Glutamate GABA and Glycine Receptors Are Transmembrane Proteins Encoded by Two Distinct Gene Families
	- [ ] Chloride Currents Through GABA, and Glycine Receptor-Channels Normally Inhibit the Postsynaptic Cell
- [ ] Some Synaptic Actions in the CNS Depend on Other Types of IOnotropic Receptors
- [ ] Excitatory and Inhibitory Synaptic Actions Are Integrated by Neurons Into a Single Output
	- [ ] Synaptic Inputs Are Integrated at the Axon Initial Segment
	- [ ] Subclasses of GABAergic Neurons Neurons Target Distinct Regions of Their Postsynaptic Target Neurons to Produce Inhibitory Actions With Different Functions
	- [ ] Dendrites Are Electrically Excitable Structures That Can Amplify Synaptic Input

## 14 Modulation of Synaptic Transmission and Neuronal Excitability: Second Messengers
* [ ] The Cyclic AMP Pathway Is the Best Understood Second-Messenger Signaling Cascade Initiated by G Protein-Coupled Receptors
* [ ] The Second-Messenger Pathways Initiated by G Protein-Coupled Receptors Share a Common Molecular Logic
	* [ ] A Family of G Proteins Activates Distinct Second-Messenger Pathways
	* [ ] Hydrolysis of Phospholipids by Phospholipase C Produces Two Important Second Messengers, $IP_3$ and Diacylglycerol
* [ ] Receptor Tyrosine Kinases Compose the Second Major Family of Metabotropic Receptors
* [ ] Several Classes of Metabolites Can Serve as Transcellular Messengers
	* [ ] Hydrolysis of Phospholipids by Phospholipase $A_2$ Liberates Arachidonic Acid to Produce Other Second Messengers
	* [ ] Endocannabinoids Are Transcellular Messengers That Inhibit Presynaptic Transmitter Release
	* [ ] The Gaseous Second Messenger Nitric Oxide Is a Transcellular Signal That Stimulates Stimulates Cyclic GMP Synthesis
* [ ] The Physiological Actions of Metabotropic Receptors Differ From Those of Ionotropic Receptors
	* [ ] Second-Messenger Cascades Can Increase or Decrease the Opening of Many Types of Ion Channels
	* [ ] G Proteins Can Modulate Ion Channels Directly
	* [ ] Cyclic AMP-Dependent Protein Phosphorylation Can Close Potassium Channels
* [ ] Second Messengers Can Endow Synaptic Transmission with Long-Lasting Consequences
* [ ] Modulators Can Influence Circuit Function by Altering Intrinsic Excitability of Synaptic Strength
	* [ ] Multiple Neuromodulators Can Converge Onto the Same Neuron and Ion Channels 
	* [ ] Why So Many Modulators?

## 15 Transmitter Release
- [ ] Transmitter Release is Regulated by Depolarization of the Presynaptic Terminal
- [ ] Release Is Triggered by Calcium Influx
	- [ ] The Relation Between Presynaptic Calcium Concentration and Release
	- [ ] Several Classes of Calcium Channels Mediate Transmitter Release
- [ ] Transmitter Is Released in Quantal Units
- [ ] Transmitter Is Store and Released by Synaptic Vesicles
	- [ ] Synaptic Vesicles Discharge Transmitter by Exocytosis and Are Recycled by Endocytosis
	- [ ] Capacitance Measurements Provide Insights Into the Kinetics of Exocytosis and Endocytosis
	- [ ] Exocytosis Involved the Formation of a Temporary Fusion Pore
	- [ ] The Synaptic Vesicle Cycle Involves Several Steps
- [ ] Exocytosis of Synaptic Vesicle Relies on a Highly Conserved Protein Machinery
	- [ ] The Synapsins Are Important for Vesicle Restraint and Mobilization 
	- [ ] SNARE Proteins Catalyze Fusion Vesicles with the Plasma Membrane
	- [ ] Calcium Binding to Synaptotagmin  Triggers Transmitter Release
	- [ ] The Fusion Machinery Is Embedded in a Conserved Protein Scaffold at the Active Zone
- [ ] Modulation of Transmitter Release Underlies Synaptic Plasticity
	- [ ] Activity-Dependent Changes in Intracellular Free Calcium Can Produce Long-Lasting Changes in Release
	- [ ] Axo-axonic Synapses on Presynaptic Terminals Regulate Transmitter Release

## 16 Neurotransmitters
- [ ] A Chemical Messenger Must Meet Four Criteria to Be Considered a Neurotransmitter
- [ ] Only a Few Small-Molecule Substances Act as Transmitters
	- [ ] Acetylcholine
	- [ ] Biogenic Amine Transmitters
	- [ ] Amino Acid Transmitters
	- [ ] ATP and Adenosine
- [ ] Small Molecule Transmitters Are Actively Taken Up Into Vesicles
- [ ] Many Neuroactive Peptides Serve as Transmitters
- [ ] Peptides and Small-Molecule Transmitters Differ in Several Ways
- [ ] Peptides and Small-Molecule Transmitters Can Be Co-released
- [ ] Removal of Transmitter From the Synaptic Cleft Terminates Synaptic Transmission

# Part IV - Perception

## 17 Sensory Coding
- [ ] Psychophysics Relates Sensations to the Physical Properties of Stimuli
	- [ ] Psychophysics Quantifies the Perception of Stimulus Properties
- [ ] Stimuli Are Represented in the Nervous System by Firing Patterns of Neurons
	- [ ] Sensory Receptors Respond to Specific Classes of Stimulus Energy
	- [ ] Multiple Subclasses of Sensory Receptors Are Found in Each Sense Organ
	- [ ] Receptor Population Codes Transmit Sensory Information to the Brain
	- [ ] Sequences of Action Potentials Signal the Temporal Dynamics of Stimuli
	- [ ] The Receptive Fields of Sensory Neurons Provide Spatial Information About Stimulus Location
- [ ] Central Nervous System Circuits Refine Sensory Information
	- [ ] The Receptor Surface Is Represented Topographically in the Early Stages of Each Sensory System
	- [ ] Sensory Information Is Processed in Parallel Pathways in the Cerebral Cortex
	- [ ] Feedback Pathways From the Brain Regulate Sensory Coding Mechanisms
	- [ ] Top-Down Learning Mechanisms Influence Sensory Processing

## 18 Receptors of the Somatosensory System
- [ ] Dorsal Root Ganglion Neurons Are the Primary Sensory Receptor Cells of the Somatosensory System
- [ ] Peripheral Somatosensory Nerve Fibers Conduct Action Potentials at Different Rates
- [ ] A Variety of Specialized Receptors Are Employed by the Somatosensory System
	- [ ] Mechanoreceptors Mediate Touch and Proprioception
	- [ ] Specialized End Organs Contribute to Mechanosensation
	- [ ] Proprioceptors Measure Muscle Activity and Join Positions
	- [ ] Thermal Receptors Detect Changes in Skin Temperature
	- [ ] Nociceptors Mediate Pain
	- [ ] Itch Is a Distinctive Cutaneous Sensation
	- [ ] Visceral Sensations Present the Status of Internal Organs
- [ ] Action Potential Codes Transmit Somatosensory Information to the Brain
	- [ ] Sensory Ganglia Provide a Snapshot of Population Responses to Somatic Stimuli
	- [ ] Somatosensory Information Enters the Central Nervous System Via Spinal or Cranial Nerves

## 19 Touch