"""Configuration for the gitcoin scorer"""

# Weight values for each stamp based on its perceived significance in assessing the unique humanity of the Passport holder
GITCOIN_PASSPORT_WEIGHTS = {
    "BeginnerCommunityStaker": "1.513",
    "Brightid": "0.802",
    "CivicCaptchaPass": "1.014",
    "CivicLivenessPass": "3.004",
    "CivicUniquenessPass": "6.005",
    "CoinbaseDualVerification": "16.042",
    "Discord": "0.516",
    "Ens": "0.408",
    "ETHDaysActive#50": "0.507",
    "ETHGasSpent#0.25": "1.003",
    "ETHnumTransactions#100": "0.51",
    "ETHScore#50": "10.012",
    "ETHScore#75": "2.001",
    "ETHScore#90": "2.009",
    "ExperiencedCommunityStaker": "2.515",
    "GitcoinContributorStatistics#totalContributionAmountGte#1000": "5.018",
    "GitcoinContributorStatistics#totalContributionAmountGte#100": "2.017",
    "GitcoinContributorStatistics#totalContributionAmountGte#10": "0.523",
    "githubContributionActivityGte#120": "3.019",
    "githubContributionActivityGte#30": "2.020",
    "githubContributionActivityGte#60": "2.021",
    "GnosisSafe": "0.822",
    "Google": "0.525",
    "GuildAdmin": "0.724",
    "GuildPassportMember": "0.54",
    "HolonymGovIdProvider": "16.026",
    "IdenaState#Human": "2.027",
    "IdenaState#Newbie": "6.028",
    "IdenaState#Verified": "2.029",
    "Lens": "0.93",
    "Linkedin": "1.531",
    "NFT": "1.032",
    "NFTScore#50": "10.033",
    "NFTScore#75": "2.034",
    "NFTScore#90": "2.035",
    "SelfStakingBronze": "1.036",
    "SelfStakingGold": "3.037",
    "SelfStakingSilver": "2.038",
    "SnapshotProposalsProvider": "0.839",
    "TrustaLabs": "0.511",
    "TrustedCitizen": "4.041",
    "ZkSyncEra": "0.606",
    "zkSyncScore#20": "1.67",
    "zkSyncScore#50": "1.67",
    "zkSyncScore#5": "1.67",
    "Outdid": "10",
    "BinanceBABT": "16.021",
}


# The Boolean scorer deems Passport holders unique humans if they meet or exceed the below thresholdold
GITCOIN_PASSPORT_THRESHOLD = "20"


def increment_scores(increment_value):
    for key, value in GITCOIN_PASSPORT_WEIGHTS.copy().items():
        updated_value = float(value) + increment_value
        print(f'"{key}": "{updated_value:.6f}",')
