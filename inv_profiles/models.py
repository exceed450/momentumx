from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    A single investment profile containing all
    the information about the investment
    """
    EXCHANGE_CHOICES = [
        ('NDAQ', 'NASDAQ'),
        ('OSEBX', 'Oslo stock exchange'),
    ]

    RATING_CHOICES = [
        ('1', 'Excellent'),
        ('2', 'Very good'),
        ('3', 'Good'),
        ('4', 'Poor'),
        ('5', 'Very poor'),
    ]

    MOMENTUM_CHOICES = [
        ('1', 'Excellent performing stock'),
        ('2', 'Strong performing stock'),
        ('3', 'Average performing stock'),
        ('4', 'Slow performing stock'),
        ('5', 'Poor performing stock'),
    ]

    INVESTMENT_TYPE_CHOICES = [
        ('1', 'Growth stock investment'),
        ('2', 'Value stock investment'),
        ('3', 'Trading investment'),
        ('4', 'Day trade investment'),
    ]

    INVESTMENT_STATUS_CHOICES = [
        ('1', 'Good standing'),
        ('2', 'Watch closely'),
        ('3', 'Needs to be replaced'),
    ]

    TECH_ENTRY_CHOICES = [
        ('1', 'Good entry at this time'),
        ('2', 'Might be good entry soon'),
        ('3', 'Not a good entry at this time'),
    ]

    FUNDAMENTAL_ENTRY_CHOICES = [
        ('1', 'Excellent fundamentals'),
        ('2', 'Good fundamentals'),
        ('3', 'Average fundamentals'),
        ('4', 'Terrible fundamentals'),
    ]

    INVESTMENT_DECISION_CHOICES = [
        ('1', 'Invested'),
        ('2', 'Approved'),
        ('3', 'On watchlist'),
        ('4', 'Rejected'),
    ]

    company = models.CharField(max_length=200)
    exchange = models.CharField(max_length=200,
                                choices=EXCHANGE_CHOICES,
                                default="None")
    ticker = models.CharField(max_length=10,
                              default="None")
    rating = models.CharField(max_length=50,
                              choices=RATING_CHOICES,
                              default="None")
    stock_momentum = models.CharField(max_length=50,
                                      choices=MOMENTUM_CHOICES,
                                      default="None")
    investment_type = models.CharField(max_length=50,
                                       choices=INVESTMENT_TYPE_CHOICES,
                                       default="None")
    investment_status = models.CharField(max_length=50,
                                         choices=INVESTMENT_STATUS_CHOICES,
                                         default="None")
    investment_decision = models.CharField(max_length=50,
                                           choices=INVESTMENT_DECISION_CHOICES,
                                           default="None")
    tech_analysis_opinion = models.CharField(max_length=50,
                                             choices=TECH_ENTRY_CHOICES,
                                             default="None")
    fundamental_analysis_opinion = models.CharField(max_length=50,
                                                    choices=FUNDAMENTAL_ENTRY_CHOICES,
                                                    default="None")
    entry_strategy = models.CharField(max_length=250,
                                      default="No strategy defined")
    exit_strategy = models.CharField(max_length=250,
                                     default="No strategy defined")
    general_notes = models.CharField(max_length=250,
                                     default="", 
                                     blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    shared = models.BooleanField(default=False)

    def __str__(self):
        return self.company


class Report(models.Model):
    """ Reports related to the investment """
    REPORT_TYPE_CHOICES = [
        ('1', 'Earnings report - quarterly'),
        ('2', 'Earnings report - annual'),
        ('3', 'Sales report'),
        ('4', 'Traffic report'),
        ('5', 'Other'),
    ]

    title = models.CharField(max_length=250)
    report_type = models.CharField(max_length=150,
                                   choices=REPORT_TYPE_CHOICES)
    link = models.URLField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)


class Transaction(models.Model):
    """
    A transaction representing:
        - Buying a stock
        - Selling a stock
        - Dividend payout
        - Tax payment
        - Tax payout
        - Interest payment
        - Interest payout
    """
    TX_TYPE_CHOICES = [
        ('1', 'Stock purchase'),
        ('2', 'Stock sold'),
        ('3', 'Dividend payout'),
        ('4', 'Tax payout'),
        ('5', 'Tax payment'),
        ('6', 'Interest payment'),
        ('7', 'Interest payout'),
    ]
    type_of_transaction = models.CharField(max_length=100,
                                           choices=TX_TYPE_CHOICES)
    amount = models.CharField(max_length=100)
    date_of_transaction = models.DateField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)


class Segment(models.Model):
    """ Represents a business segment of a company """
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    part_of_revenue = models.CharField(max_length=200)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)


class News(models.Model):
    """ Represents a news article """
    SIGNIFICANCE_CHOICES = [
        ('1', 'News of high interest'),
        ('2', 'News of medium interest'),
        ('3', 'News of low interest'),
    ]
    title = models.CharField(max_length=250)
    summary = models.CharField(max_length=250)
    significance = models.CharField(max_length=100,
                                    choices=SIGNIFICANCE_CHOICES)
    link = models.URLField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)


class Risk(models.Model):
    """ Represents a risk for a company """
    RATING_CHOICES = [
        ('1', 'High impact'),
        ('2', 'Medium impact'),
        ('3', 'Low impact'),
    ]

    title = models.CharField(max_length=250)
    rating = models.CharField(max_length=250,
                              choices=RATING_CHOICES)
    notes = models.CharField(max_length=250)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)


class KeyMetric(models.Model):
    """ Represents a key metric for a company """
    title = models.CharField(max_length=250)
    type_of_metric = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    link = models.CharField(max_length=500)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)


class RevenueIncomeSources(models.Model):
    """ Represents a revenue or income stream for a company """
    SOURCES_TYPE_CHOICES = [
        ('1', 'Revenue'),
        ('2', 'Income'),
    ]

    SOURCE_FREQ_CHOICES = [
        ('1', 'Recurring'),
        ('2', 'One-time'),
    ]

    type_of_source = models.CharField(max_length=250,
                                      choices=SOURCES_TYPE_CHOICES)
    source_frequency = models.CharField(max_length=250,
                                        choices=SOURCE_FREQ_CHOICES)
    description = models.CharField(max_length=250)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)


class Competitor(models.Model):
    """ Represents a competitor in the industry the company is locatated in """
    COMPETITOR_IMP_CHOICES = [
        ('1', 'Biggest competitor'),
        ('2', 'Medium competitor'),
        ('3', 'Small competitor'),
    ]
    name = models.CharField(max_length=250)
    competitor_impact = models.CharField(max_length=50,
                                         choices=COMPETITOR_IMP_CHOICES)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)


class BrokerAnalysis(models.Model):
    """ Representing an analysis from an official broker """
    title = models.CharField(max_length=250)
    broker = models.CharField(max_length=250)
    analyst = models.CharField(max_length=250)
    link = models.CharField(max_length=250)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
