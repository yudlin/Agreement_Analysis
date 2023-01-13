def agreement(S1, S2, Ana=1, sFig=True):
     '''
     This program is used for the agreement evaluation between two methods
     and the test for repeatability. Please note, for the cases of measuring
     agreement in repeated measurements, the correction method is not coveded
     in the code.
     Designed by Yue-Der Lin, Feng Chia University, Taiwan.

     Reference:
        J. M. Bland and D. G. Altman, "Statistical methods for assessing
        agreement between two methods of clinical measurement", Lancet,
        1986,i, pp.307-310.

     Inputs:
         S1    Measured data, an (N1, ) array.
         S2    Ground truth data, an (N2, ) array, N2 = N1.
        Ana    1 = Agreement analysis (default),
               2 = Repeatability test.
       sFig    True = Show the figures, False = Do not show the figures
               (default = True).

     Output:
      d_bar    Mean of the bias (difference).
      coref    Pearson's correlation coefficient.
      UpLimit  Upper limit of agreement.
      LoLimit  Lower limit of agreement.

     Usage example: (assume you have S1 and S2)
        from agreement import agreement
        d_bar, coref, UpLimit, LoLimit = agreement(S1, S2, 1, True)
     '''
     # Import modules:
     import matplotlib
     import matplotlib.pyplot as plt
     import numpy as np
     import scipy.stats

     # Initialization:
     N1 = np.size(S1); N2 = np.size(S2)
     N = np.min([N1, N2])
     X1 = S1[np.arange(N)]; X2 = S2[np.arange(N)]
     matplotlib.rcParams['font.family'] = 'Times'

     # Pearson's Correlation Coefficient:
     (coref, _) = scipy.stats.pearsonr(X1, X2)
     print("Pearson's Correlation Coefficient = %7.4f" % coref, end="\n")

     if Ana == 2: # Repeatability test
        print("Repeatability Test:", end="\n")
        S1 = X1-X2; S2 = (X1+X2)/2
        d_bar = np.mean(S1) # Mean difference.
        s = np.std(S1)      # S.D. of the difference.
        Up = 1.96*s; Lo = -1.96*s
        UpLimit = d_bar + Up; LoLimit = d_bar + Lo
        D_bar = d_bar*np.ones(N)
        Cp = UpLimit*np.ones(N)
        Cn = LoLimit*np.ones(N)
        print("  mean of the bias (difference) = ", d_bar, end="\n")
        print("  S.D. of the bias (difference) = ", s, end="\n")
        print("    Coefficient of repeatability = ", 2*s, end="\n")

        # Percentage for the differences located within -1.96*s and 1.96*s:
        cnt = 0
        for k in range(N):
            if S1[k] > LoLimit and S1[k] < UpLimit:
                cnt = cnt + 1
        pcnt = 100*cnt/N
        print("  Percentage within Mean+-1.96*S.D. = "  , pcnt, end="\n")
        if pcnt >= 95:
            print('  The method is evaluated to be "Repeatable".', end="\n")
        else:
            print('  The method is evaluated to be "Not Repeatable".', end="\n")

     else: # Agreement analysis
        print("Agreement Analysis:", end="\n")
        S1 = X1-X2; S2 = (X1+X2)/2
        d_bar = np.mean(S1) # Mean difference.
        s = np.std(S1)      # S.D. of the difference.
        Up = 1.96*s; Lo = -1.96*s
        UpLimit = d_bar + Up; LoLimit = d_bar + Lo
        D_bar = d_bar*np.ones(N)
        Cp = UpLimit*np.ones(N)
        Cn = LoLimit*np.ones(N)
        print("  mean of the difference = ", d_bar, end="\n")
        print("  S.D. of the difference = ", s, end="\n")
        print("    Upper limit of agreement = ", UpLimit, end="\n")
        print("    Lower limit of agreement = ", LoLimit, end="\n")

        # Percentage for the differences located within -1.96*s and 1.96*s:
        cnt = 0
        for k in range(N):
            if S1[k] > LoLimit and S1[k] < UpLimit:
                cnt = cnt + 1
        pcnt = 100*cnt/N
        print("  Percentage within Mean+-1.96*S.D. = "  , pcnt, end="\n")

        if sFig == True:
            # Plot the scatter diagram:
            plt.figure(1, figsize = (7.2, 5.4))
            plt.plot(X2, X1, 'k.', X2, X2, 'b-')
            plt.xlabel('Ground Truth', fontsize = 13)
            plt.ylabel('Measured', fontsize = 13)
            plt.title('Scatter Diagram', fontsize = 15)
            plt.savefig('Fig_Scatter_Diagram.jpg', dpi=1200, transparent=True)
            # Bland-Altman plot:
            plt.figure(2, figsize = (7.2, 5.4))
            plt.plot(S2, S1, 'k.', S2, D_bar, 'b-', S2, Cp, 'm-', S2, Cn, 'm-')
            plt.xlabel('Mean of Methods', fontsize = 13)
            plt.ylabel('Difference between Methods', fontsize = 13)
            plt.title('Bland-Altman Plot', fontsize = 15)
            plt.savefig('Fig_Bland_Altman_Plot.jpg', dpi=1200, transparent=True)

     return d_bar, coref, UpLimit, LoLimit