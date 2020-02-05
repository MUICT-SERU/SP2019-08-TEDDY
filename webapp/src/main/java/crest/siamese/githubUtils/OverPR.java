package crest.siamese.githubUtils;

public class OverPR
{
    private PullRequest PRWhole;

    public PullRequest getPRWhole() {
        return PRWhole;
    }

    public void setPRWhole(PullRequest PRWhole) {
        this.PRWhole = PRWhole;
    }

    public OverPR(PullRequest PRWhole) {
        this.PRWhole = PRWhole;
    }
}
