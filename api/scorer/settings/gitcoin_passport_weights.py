"""Configuration for the gitcoin scorer"""

# Weight values for each stamp based on its perceived significance in assessing the unique humanity of the Passport holder
GITCOIN_PASSPORT_WEIGHTS = {
    "Brightid": "0",
    "CommunityStakingBronze": "2.29",
    "CommunityStakingGold": "0.83",
    "CommunityStakingSilver": "0.83",
    "Coinbase": "1.67",
    "Discord": "1.67",
    "Ens": "2.4",
    "EthGTEOneTxnProvider": "1.56",
    "EthGasProvider": "1.56",
    "ethPossessionsGte#1": "1.77",
    "ethPossessionsGte#10": "2.81",
    "ethPossessionsGte#32": "1.04",
    "Facebook": "0.52",
    "FacebookFriends": "0.83",
    "FacebookProfilePicture": "0.83",
    "FiftyOrMoreGithubFollowers": "3.12",
    "FirstEthTxnProvider": "1.67",
    "FiveOrMoreGithubRepos": "1.77",
    "ForkedGithubRepoProvider": "1.77",
    "GitcoinContributorStatistics#numGr14ContributionsGte#1": "1.77",
    "GitcoinContributorStatistics#numGrantsContributeToGte#1": "1.67",
    "GitcoinContributorStatistics#numGrantsContributeToGte#10": "1.67",
    "GitcoinContributorStatistics#numGrantsContributeToGte#100": "0",
    "GitcoinContributorStatistics#numGrantsContributeToGte#25": "1.56",
    "GitcoinContributorStatistics#numRoundsContributedToGte#1": "1.67",
    "GitcoinContributorStatistics#totalContributionAmountGte#10": "1.77",
    "GitcoinContributorStatistics#totalContributionAmountGte#100": "1.67",
    "GitcoinContributorStatistics#totalContributionAmountGte#1000": "1.98",
    "GitcoinGranteeStatistics#numGrantContributors#10": "1.98",
    "GitcoinGranteeStatistics#numGrantContributors#100": "2.4",
    "GitcoinGranteeStatistics#numGrantContributors#25": "2.29",
    "GitcoinGranteeStatistics#numGrantsInEcoAndCauseRound#1": "3.44",
    "GitcoinGranteeStatistics#numOwnedGrants#1": "2.81",
    "GitcoinGranteeStatistics#totalContributionAmount#100": "2.6",
    "GitcoinGranteeStatistics#totalContributionAmount#1000": "1.04",
    "GitcoinGranteeStatistics#totalContributionAmount#10000": "0.52",
    "Github": "0.52",
    "GitPOAP": "2.92",
    "GnosisSafe": "1.67",
    "Google": "1.67",
    "gtcPossessionsGte#10": "1.67",
    "gtcPossessionsGte#100": "1.77",
    "Lens": "1.77",
    "Linkedin": "1.77",
    "NFT": "1.67",
    "POAP": "1.67",
    "Poh": "1.77",
    "SelfStakingBronze": "2.78",
    "SelfStakingGold": "1.56",
    "SelfStakingSilver": "0.58",
    "SnapshotProposalsProvider": "1.67",
    "SnapshotVotesProvider": "1.77",
    "StarredGithubRepoProvider": "1.67",
    "TenOrMoreGithubFollowers": "2.4",
    "Twitter": "0.52",
    "TwitterFollowerGT100": "1.67",
    "TwitterFollowerGT500": "1.67",
    "TwitterFollowerGT5000": "0",
    "TwitterFollowerGTE1000": "1.77",
    "TwitterTweetGT10": "1.67",
    "YupScore": "0",
    "ZkSync": "1.67",
}


# The Boolean scorer deems Passport holders unique humans if they meet or exceed the below thresholdold
GITCOIN_PASSPORT_THRESHOLD = "15"
