# Expose base classses
from .base import DataLoader
from .base import SentenceDataset
from .base import StringDataset
from .base import MongoDataset

# Expose all sequence labeling datasets
from .sequence_labeling import ColumnCorpus
from .sequence_labeling import ColumnDataset
# standard NER datasets
from .sequence_labeling import CONLL_03
from .sequence_labeling import CONLL_03_GERMAN
from .sequence_labeling import CONLL_03_DUTCH
from .sequence_labeling import CONLL_03_SPANISH
from .sequence_labeling import CONLL_2000
from .sequence_labeling import BIOSCOPE
from .sequence_labeling import WNUT_17
# other NER datasets
from .sequence_labeling import NER_ARABIC_ANER
from .sequence_labeling import NER_ARABIC_AQMAR
from .sequence_labeling import NER_BASQUE
from .sequence_labeling import NER_CHINESE_WEIBO
from .sequence_labeling import NER_DANISH_DANE
from .sequence_labeling import NER_ENGLISH_MOVIE_SIMPLE
from .sequence_labeling import NER_ENGLISH_MOVIE_COMPLEX
from .sequence_labeling import NER_ENGLISH_PERSON
from .sequence_labeling import NER_ENGLISH_RESTAURANT
from .sequence_labeling import NER_ENGLISH_SEC_FILLINGS
from .sequence_labeling import NER_ENGLISH_STACKOVERFLOW
from .sequence_labeling import NER_ENGLISH_TWITTER
from .sequence_labeling import NER_ENGLISH_WIKIGOLD
from .sequence_labeling import NER_ENGLISH_WNUT_2020
from .sequence_labeling import NER_ENGLISH_WEBPAGES
from .sequence_labeling import NER_FINNISH
from .sequence_labeling import NER_GERMAN_BIOFID
from .sequence_labeling import NER_GERMAN_EUROPARL
from .sequence_labeling import NER_GERMAN_GERMEVAL
from .sequence_labeling import NER_GERMAN_LEGAL
from .sequence_labeling import NER_GERMAN_POLITICS
from .sequence_labeling import NER_HUNGARIAN
from .sequence_labeling import NER_ICELANDIC
from .sequence_labeling import NER_JAPANESE
from .sequence_labeling import NER_MASAKHANE
from .sequence_labeling import NER_MULTI_WIKINER
from .sequence_labeling import NER_MULTI_WIKIANN
from .sequence_labeling import NER_MULTI_XTREME
from .sequence_labeling import NER_SWEDISH
from .sequence_labeling import NER_TURKU
# keyphrase detection datasets
from .sequence_labeling import KEYPHRASE_INSPEC
from .sequence_labeling import KEYPHRASE_SEMEVAL2010
from .sequence_labeling import KEYPHRASE_SEMEVAL2017
# word sense disambiugation
from .sequence_labeling import WSD_UFSAC
# universal proposition banks
from .sequence_labeling import UP_CHINESE
from .sequence_labeling import UP_ENGLISH
from .sequence_labeling import UP_FINNISH
from .sequence_labeling import UP_FRENCH
from .sequence_labeling import UP_GERMAN
from .sequence_labeling import UP_ITALIAN
from .sequence_labeling import UP_SPANISH
from .sequence_labeling import UP_SPANISH_ANCORA

# Expose all entity linking datasets
from .entity_linking import EntityLinkingCorpus
from .entity_linking import NEL_ENGLISH_AIDA
from .entity_linking import NEL_ENGLISH_AQUAINT
from .entity_linking import NEL_ENGLISH_IITB
from .entity_linking import NEL_ENGLISH_REDDIT
from .entity_linking import NEL_ENGLISH_TWEEKI
from .entity_linking import NEL_GERMAN_HIPE

# Expose all document classification datasets
from .document_classification import ClassificationCorpus
from .document_classification import ClassificationDataset
from .document_classification import CSVClassificationCorpus
from .document_classification import CSVClassificationDataset
from .document_classification import AMAZON_REVIEWS
from .document_classification import COMMUNICATIVE_FUNCTIONS
from .document_classification import GERMEVAL_2018_OFFENSIVE_LANGUAGE
from .document_classification import GLUE_COLA
from .document_classification import GO_EMOTIONS
from .document_classification import IMDB
from .document_classification import NEWSGROUPS
from .document_classification import SENTIMENT_140
from .document_classification import SENTEVAL_CR
from .document_classification import SENTEVAL_MR
from .document_classification import SENTEVAL_MPQA
from .document_classification import SENTEVAL_SUBJ
from .document_classification import SENTEVAL_SST_BINARY
from .document_classification import SENTEVAL_SST_GRANULAR
from .document_classification import TREC_50
from .document_classification import TREC_6
from .document_classification import WASSA_ANGER
from .document_classification import WASSA_FEAR
from .document_classification import WASSA_JOY
from .document_classification import WASSA_SADNESS
from .document_classification import YAHOO_ANSWERS

# Expose all treebanks
from .treebanks import UniversalDependenciesCorpus
from .treebanks import UniversalDependenciesDataset
from .treebanks import UD_ARMENIAN
from .treebanks import UD_ENGLISH
from .treebanks import UD_ANCIENT_GREEK
from .treebanks import UD_KAZAKH
from .treebanks import UD_ESTONIAN
from .treebanks import UD_GERMAN
from .treebanks import UD_GERMAN_HDT
from .treebanks import UD_DUTCH
from .treebanks import UD_FAROESE
from .treebanks import UD_FRENCH
from .treebanks import UD_ITALIAN
from .treebanks import UD_SPANISH
from .treebanks import UD_PORTUGUESE
from .treebanks import UD_ROMANIAN
from .treebanks import UD_CATALAN
from .treebanks import UD_POLISH
from .treebanks import UD_CZECH
from .treebanks import UD_SLOVAK
from .treebanks import UD_SWEDISH
from .treebanks import UD_DANISH
from .treebanks import UD_NORWEGIAN
from .treebanks import UD_FINNISH
from .treebanks import UD_SLOVENIAN
from .treebanks import UD_CROATIAN
from .treebanks import UD_SERBIAN
from .treebanks import UD_BULGARIAN
from .treebanks import UD_ARABIC
from .treebanks import UD_HEBREW
from .treebanks import UD_TURKISH
from .treebanks import UD_PERSIAN
from .treebanks import UD_RUSSIAN
from .treebanks import UD_HINDI
from .treebanks import UD_INDONESIAN
from .treebanks import UD_JAPANESE
from .treebanks import UD_CHINESE
from .treebanks import UD_KOREAN
from .treebanks import UD_BASQUE
from .treebanks import UD_GREEK
from .treebanks import UD_LIVVI
from .treebanks import UD_NORTH_SAMI
from .treebanks import UD_MARATHI
from .treebanks import UD_MALTESE
from .treebanks import UD_AFRIKAANS
from .treebanks import UD_OLD_FRENCH
from .treebanks import UD_GOTHIC
from .treebanks import UD_WOLOF
from .treebanks import UD_BELARUSIAN
from .treebanks import UD_OLD_CHURCH_SLAVONIC
from .treebanks import UD_COPTIC
from .treebanks import UD_IRISH
from .treebanks import UD_LATVIAN
from .treebanks import UD_LITHUANIAN
from .treebanks import UD_GALICIAN

# Expose all text-text datasets
from .text_text import ParallelTextCorpus
from .text_text import ParallelTextDataset
from .text_text import OpusParallelCorpus
from .text_text import DataPairDataset
from .text_text import DataPairCorpus
from .text_text import GLUE_MNLI
from .text_text import GLUE_MRPC
from .text_text import GLUE_RTE
from .text_text import GLUE_QNLI
from .text_text import GLUE_QQP
from .text_text import GLUE_WNLI
from .text_text import SUPERGLUE_RTE

# Expose all text-image datasets
from .text_image import FeideggerCorpus
from .text_image import FeideggerDataset

# Expose all biomedical data sets
from .biomedical import ANAT_EM
from .biomedical import AZDZ
from .biomedical import BIONLP2013_PC
from .biomedical import BIONLP2013_CG
from .biomedical import BIO_INFER
from .biomedical import BIOSEMANTICS
from .biomedical import BC2GM
from .biomedical import CELL_FINDER
from .biomedical import CEMP
from .biomedical import CDR
from .biomedical import CHEMDNER
from .biomedical import CRAFT
from .biomedical import CRAFT_V4
from .biomedical import CLL
from .biomedical import DECA
from .biomedical import FSU
from .biomedical import GELLUS
from .biomedical import GPRO
from .biomedical import IEPA
from .biomedical import JNLPBA
from .biomedical import LOCTEXT
from .biomedical import LINNEAUS
from .biomedical import NCBI_DISEASE
from .biomedical import MIRNA
from .biomedical import OSIRIS
from .biomedical import PDR
from .biomedical import S800
from .biomedical import SCAI_CHEMICALS
from .biomedical import SCAI_DISEASE
from .biomedical import VARIOME

# Expose all biomedical data sets using the HUNER splits
from .biomedical import HUNER_CHEMICAL
from .biomedical import HUNER_CHEMICAL_CHEBI
from .biomedical import HUNER_CHEMICAL_CHEMDNER
from .biomedical import HUNER_CHEMICAL_CDR
from .biomedical import HUNER_CHEMICAL_CEMP
from .biomedical import HUNER_CHEMICAL_SCAI
from .biomedical import HUNER_CHEMICAL_CRAFT_V4
# -
from .biomedical import HUNER_CELL_LINE
from .biomedical import HUNER_CELL_LINE_CLL
from .biomedical import HUNER_CELL_LINE_CELL_FINDER
from .biomedical import HUNER_CELL_LINE_GELLUS
from .biomedical import HUNER_CELL_LINE_JNLPBA
# -
from .biomedical import HUNER_DISEASE
from .biomedical import HUNER_DISEASE_CDR
from .biomedical import HUNER_DISEASE_MIRNA
from .biomedical import HUNER_DISEASE_NCBI
from .biomedical import HUNER_DISEASE_SCAI
from .biomedical import HUNER_DISEASE_VARIOME
from .biomedical import HUNER_DISEASE_PDR
# -
from .biomedical import HUNER_GENE
from .biomedical import HUNER_GENE_BIO_INFER
from .biomedical import HUNER_GENE_BC2GM
from .biomedical import HUNER_GENE_CHEBI
from .biomedical import HUNER_GENE_CRAFT_V4
from .biomedical import HUNER_GENE_CELL_FINDER
from .biomedical import HUNER_GENE_DECA
from .biomedical import HUNER_GENE_FSU
from .biomedical import HUNER_GENE_GPRO
from .biomedical import HUNER_GENE_IEPA
from .biomedical import HUNER_GENE_JNLPBA
from .biomedical import HUNER_GENE_LOCTEXT
from .biomedical import HUNER_GENE_MIRNA
from .biomedical import HUNER_GENE_OSIRIS
from .biomedical import HUNER_GENE_VARIOME
# -
from .biomedical import HUNER_SPECIES
from .biomedical import HUNER_SPECIES_CELL_FINDER
from .biomedical import HUNER_SPECIES_CHEBI
from .biomedical import HUNER_SPECIES_CRAFT_V4
from .biomedical import HUNER_SPECIES_LOCTEXT
from .biomedical import HUNER_SPECIES_LINNEAUS
from .biomedical import HUNER_SPECIES_MIRNA
from .biomedical import HUNER_SPECIES_S800
from .biomedical import HUNER_SPECIES_VARIOME

# Expose all biomedical data sets used for the evaluation of BioBERT
from .biomedical import BIOBERT_CHEMICAL_BC4CHEMD
from .biomedical import BIOBERT_CHEMICAL_BC5CDR
from .biomedical import BIOBERT_DISEASE_NCBI
from .biomedical import BIOBERT_DISEASE_BC5CDR
from .biomedical import BIOBERT_SPECIES_LINNAEUS
from .biomedical import BIOBERT_SPECIES_S800
from .biomedical import BIOBERT_GENE_BC2GM
from .biomedical import BIOBERT_GENE_JNLPBA
from .treebanks import UD_LATIN

# Expose all relation extraction datasets
from .relation_extraction import SEMEVAL_2010_TASK_8
from .relation_extraction import TACRED
from .relation_extraction import CoNLL04
from .relation_extraction import DRUG_PROD
