## Exercise Solutions

General polynomial function:

    def calc_poly(params, data):
        x = np.c_[[data**i for i in range(len(params))]]
        return np.dot(params, x)

Microbiome exercise:

    metadata = pd.read_excel('data/microbiome/metadata.xls', sheetname='Sheet1')

    chunks = []
    for i in range(9):
        this_file = pd.read_excel('data/microbiome/MID{0}.xls'.format(i+1), 'Sheet 1', index_col=0, header=None, names=['Taxon', 'Count'])
        this_file.columns = ['Count']
        this_file.index.name = 'Taxon'
        for m in metadata.columns:
            this_file[m] = metadata.ix[i][m]
        chunks.append(this_file)

    pd.concat(chunks)

Titanic proportions:

    titanic = pd.read_excel("data/titanic.xls", "titanic")

    titanic.groupby('sex')['survived'].mean()

    titanic.groupby(['pclass','sex'])['survived'].mean()

    titanic['agecat'] = pd.cut(titanic.age, [0, 13, 20, 64, 100], labels=['child', 'adolescent', 'adult', 'senior'])
    titanic.groupby(['agecat', 'pclass','sex'])['survived'].mean()

Survivor KDE plots:

    surv = dict(list(titanic.groupby('survived')))
    for s in surv:
        surv[s]['age'].dropna().plot(kind='kde', label=bool(s)*'survived' or 'died', grid=False)
    legend()
    xlim(0,100)

OBP:

    baseball[['h','bb', 'hbp']].sum(axis=1).div(
            baseball[['bb', 'hbp','ab', 'sf']].sum(axis=1)
                                ).order(ascending=False)

Cervical dystonia estimation:

    norm_like = lambda theta, x: -np.log(norm.pdf(x, theta[0], theta[1])).sum()

    fmin(norm_like, np.array([1,2]), args=(cdystonia.twstrs[(cdystonia.obs==6) & (cdystonia.treat=='Placebo')],))
    fmin(norm_like, np.array([1,2]), args=(cdystonia.twstrs[(cdystonia.obs==6) & (cdystonia.treat=='5000U')],))

Cervical dystonia bootstrapping:

    x = cdystonia.twstrs[(cdystonia.obs==6) & (cdystonia.treat=='Placebo') & (cdystonia.twstrs.notnull())].values
    n = len(x)
    s = [x[np.random.randint(0,n,n)].mean() for i in range(R)]
    placebo_mean = np.sum(s)/R

    s_sorted = np.sort(s)
    alpha = 0.05
    s_sorted[[(R+1)*alpha/2, (R+1)*(1-alpha/2)]]