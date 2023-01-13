# Agreement_Analysis
Bland-Altman Agreement Analysis

        This program is used for the agreement evaluation between two methods
        and the test for repeatability. 
        
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
