# Import all individual agent classes for easy access

# Leadership Core
from src.agents.individual.founder import Founder
from src.agents.individual.ceo import CEO
from src.agents.individual.cto_cai import CTO_CAI
from src.agents.individual.cmo_cso import CMO_CSO

# Operations & Strategy
from src.agents.individual.finance_legal_manager import FinanceLegalManager
from src.agents.individual.business_strategy_manager import BusinessStrategyManager
from src.agents.individual.technical_architecture_manager import TechnicalArchitectureManager
from src.agents.individual.devops_data_science_manager import DevOpsDataScienceManager
from src.agents.individual.digital_marketing_sales_manager import DigitalMarketingSalesManager
from src.agents.individual.customer_engagement_growth_manager import CustomerEngagementGrowthManager

# Finance & Legal Specialists
from src.agents.individual.finance_analyst import FinanceAnalyst
from src.agents.individual.legal_compliance_specialist import LegalComplianceSpecialist

# Business Strategy Specialists
from src.agents.individual.strategy_analyst import StrategyAnalyst
from src.agents.individual.investor_communications_specialist import InvestorCommunicationsSpecialist
from src.agents.individual.market_research_analyst import MarketResearchAnalyst

# Technical Architecture Specialists
from src.agents.individual.software_architecture_lead import SoftwareArchitectureLead
from src.agents.individual.ai_research_lead import AIResearchLead

# DevOps & Data Science Specialists
from src.agents.individual.devops_specialist import DevOpsSpecialist
from src.agents.individual.data_engineer import DataEngineer
from src.agents.individual.machine_learning_engineer import MachineLearningEngineer

# Marketing & Sales Specialists
from src.agents.individual.seo_sem_specialist import SEOSEMSpecialist
from src.agents.individual.sales_operations_specialist import SalesOperationsSpecialist

# Customer Engagement & Growth Specialists
from src.agents.individual.retention_specialist import RetentionSpecialist
from src.agents.individual.user_feedback_analyst import UserFeedbackAnalyst
from src.agents.individual.social_media_campaign_specialist import SocialMediaCampaignSpecialist

# List of all agents for easy access
all_agents = [
    # Leadership Core
    Founder,
    CEO,
    CTO_CAI,
    CMO_CSO,
    
    # Operations & Strategy
    FinanceLegalManager,
    BusinessStrategyManager,
    TechnicalArchitectureManager,
    DevOpsDataScienceManager,
    DigitalMarketingSalesManager,
    CustomerEngagementGrowthManager,
    
    # Finance & Legal Specialists
    FinanceAnalyst,
    LegalComplianceSpecialist,
    
    # Business Strategy Specialists
    StrategyAnalyst,
    InvestorCommunicationsSpecialist,
    MarketResearchAnalyst,
    
    # Technical Architecture Specialists
    SoftwareArchitectureLead,
    AIResearchLead,
    
    # DevOps & Data Science Specialists
    DevOpsSpecialist,
    DataEngineer,
    MachineLearningEngineer,
    
    # Marketing & Sales Specialists
    SEOSEMSpecialist,
    SalesOperationsSpecialist,
    
    # Customer Engagement & Growth Specialists
    RetentionSpecialist,
    UserFeedbackAnalyst,
    SocialMediaCampaignSpecialist
]