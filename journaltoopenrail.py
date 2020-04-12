# NX 11.0.0.33
# Journal created by Anders Fredriksen on Fri Apr 10 20:09:20 2020 Vest-Europa (sommertid)
#
import math
import NXOpen
def main() : 

    theSession  = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    workPart.RuleManager.Reload(True)
    
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Add New Child Rule")
    
    workPart.RuleManager.CreateDynamicRule("root:", "rail", "Child", "{\n Class, Curved_Rail_; \n}", None)
    
    nErrs1 = workPart.RuleManager.DoKfUpdate(markId1)
    
    # ----------------------------------------------
    #   Menu: Fit
    # ----------------------------------------------
    workPart.ModelingViews.WorkView.Fit()
    
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()