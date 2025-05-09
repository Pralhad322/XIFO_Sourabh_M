import math

if __name__ == '__main__':

    # Mean global flow completion time vs. utilization pFabric
    lambdas = [4000, 6000, 10000, 15000, 22500, 37000, 60000]

    FCTs = [[0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]]
    row = 0

    for x in lambdas:
        file = "temp/sppifo/sppifo_evaluation/pFabric/data_mining_workload/"+str(x)+"/TCP/analysis/flow_completion.statistics"
        r = open(file, 'r')
        lines = r.readlines()
        for i, line in enumerate(lines):
            if "less_100KB_99th_fct_ms" in line:
                FCTs[row][0]=line.split("=")[1].split("\n")[0]
                break
        r.close()

        file = "temp/sppifo/sppifo_evaluation/pFabric/data_mining_workload/"+str(x)+"/DCTCP/analysis/flow_completion.statistics"
        r = open(file, 'r')
        lines = r.readlines()
        for i, line in enumerate(lines):
            if "less_100KB_99th_fct_ms" in line:
                FCTs[row][1]=line.split("=")[1].split("\n")[0]
                break
        r.close()

        file = "temp/sppifo/sppifo_evaluation/pFabric/data_mining_workload/"+str(x)+"/PIFO/analysis/flow_completion.statistics"
        r = open(file, 'r')
        lines = r.readlines()
        for i, line in enumerate(lines):
            if "less_100KB_99th_fct_ms" in line:
                FCTs[row][2]=line.split("=")[1].split("\n")[0]
                break
        r.close()

        file = "temp/sppifo/sppifo_evaluation/pFabric/data_mining_workload/"+str(x)+"/SPPIFO/analysis/flow_completion.statistics"
        r = open(file, 'r')
        lines = r.readlines()
        for i, line in enumerate(lines):
            if "less_100KB_99th_fct_ms" in line:
                FCTs[row][3]=line.split("=")[1].split("\n")[0]
                break
        r.close()

        file = "temp/sppifo/sppifo_evaluation/pFabric/data_mining_workload/"+str(x)+"/XIFO/analysis/flow_completion.statistics"
        r = open(file, 'r')
        lines = r.readlines()
        for i, line in enumerate(lines):
            if "less_100KB_99th_fct_ms" in line:
                FCTs[row][4]=line.split("=")[1].split("\n")[0]
                break
        r.close()
        row = row + 1

    w = open('projects/sppifo/plots/sppifo_evaluation/pFabric/data_mining_workload/pFabric_less_100KB_99th_fct_ms.dat', 'w')
    w.write("#      TCP    DCTCP    PIFO    SPPIFO    XIFO\n")
    w.write("4000   %s    %s    %s    %s    %s    \n" % (FCTs[0][0], FCTs[0][1], FCTs[0][2], FCTs[0][3], FCTs[0][4]))
    w.write("6000   %s    %s    %s    %s    %s    \n" % (FCTs[1][0], FCTs[1][1], FCTs[1][2], FCTs[1][3], FCTs[1][4]))
    w.write("10000   %s    %s    %s    %s    %s    \n" % (FCTs[2][0], FCTs[2][1], FCTs[2][2], FCTs[2][3], FCTs[2][4]))
    w.write("15000   %s    %s    %s    %s    %s    \n" % (FCTs[3][0], FCTs[3][1], FCTs[3][2], FCTs[3][3], FCTs[3][4]))
    w.write("22500   %s    %s    %s    %s    %s    \n" % (FCTs[4][0], FCTs[4][1], FCTs[4][2], FCTs[4][3], FCTs[4][4]))
    w.write("37000   %s    %s    %s    %s    %s    \n" % (FCTs[5][0], FCTs[5][1], FCTs[5][2], FCTs[5][3], FCTs[5][4]))
    w.write("60000   %s    %s    %s    %s    %s    \n" % (FCTs[6][0], FCTs[6][1], FCTs[6][2], FCTs[6][3], FCTs[6][4]))
    w.close()


########################################################################################################################

    # Mean global flow completion time vs. utilization pFabric
    lambdas = [4000, 6000, 10000, 15000, 22500, 37000, 60000]

    FCTs = [[0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]]
    row = 0

    for x in lambdas:
        file = "temp/sppifo/sppifo_evaluation/pFabric/data_mining_workload/"+str(x)+"/TCP/analysis/flow_completion.statistics"
        r = open(file, 'r')
        lines = r.readlines()
        for i, line in enumerate(lines):
            if "less_100KB_mean_fct_ms" in line:
                FCTs[row][0]=line.split("=")[1].split("\n")[0]
                break
        r.close()

        file = "temp/sppifo/sppifo_evaluation/pFabric/data_mining_workload/"+str(x)+"/DCTCP/analysis/flow_completion.statistics"
        r = open(file, 'r')
        lines = r.readlines()
        for i, line in enumerate(lines):
            if "less_100KB_mean_fct_ms" in line:
                FCTs[row][1]=line.split("=")[1].split("\n")[0]
                break
        r.close()

        file = "temp/sppifo/sppifo_evaluation/pFabric/data_mining_workload/"+str(x)+"/PIFO/analysis/flow_completion.statistics"
        r = open(file, 'r')
        lines = r.readlines()
        for i, line in enumerate(lines):
            if "less_100KB_mean_fct_ms" in line:
                FCTs[row][2]=line.split("=")[1].split("\n")[0]
                break
        r.close()

        file = "temp/sppifo/sppifo_evaluation/pFabric/data_mining_workload/"+str(x)+"/SPPIFO/analysis/flow_completion.statistics"
        r = open(file, 'r')
        lines = r.readlines()
        for i, line in enumerate(lines):
            if "less_100KB_mean_fct_ms" in line:
                FCTs[row][3]=line.split("=")[1].split("\n")[0]
                break
        r.close()

        file = "temp/sppifo/sppifo_evaluation/pFabric/data_mining_workload/"+str(x)+"/XIFO/analysis/flow_completion.statistics"
        r = open(file, 'r')
        lines = r.readlines()
        for i, line in enumerate(lines):
            if "less_100KB_mean_fct_ms" in line:
                FCTs[row][4]=line.split("=")[1].split("\n")[0]
                break
        r.close()
        row = row + 1

    w = open('projects/sppifo/plots/sppifo_evaluation/pFabric/data_mining_workload/pFabric_less_100KB_mean_fct_ms.dat', 'w')
    w.write("#      TCP    DCTCP    PIFO    SPPIFO    XIFO\n")
    w.write("4000   %s    %s    %s    %s    %s    \n" % (FCTs[0][0], FCTs[0][1], FCTs[0][2], FCTs[0][3], FCTs[0][4]))
    w.write("6000   %s    %s    %s    %s    %s    \n" % (FCTs[1][0], FCTs[1][1], FCTs[1][2], FCTs[1][3], FCTs[1][4]))
    w.write("10000   %s    %s    %s    %s    %s    \n" % (FCTs[2][0], FCTs[2][1], FCTs[2][2], FCTs[2][3], FCTs[2][4]))
    w.write("15000   %s    %s    %s    %s    %s    \n" % (FCTs[3][0], FCTs[3][1], FCTs[3][2], FCTs[3][3], FCTs[3][4]))
    w.write("22500   %s    %s    %s    %s    %s    \n" % (FCTs[4][0], FCTs[4][1], FCTs[4][2], FCTs[4][3], FCTs[4][4]))
    w.write("37000   %s    %s    %s    %s    %s    \n" % (FCTs[5][0], FCTs[5][1], FCTs[5][2], FCTs[5][3], FCTs[5][4]))
    w.write("60000   %s    %s    %s    %s    %s    \n" % (FCTs[6][0], FCTs[6][1], FCTs[6][2], FCTs[6][3], FCTs[6][4]))
    w.close()

########################################################################################################################

    # Mean global flow completion time vs. utilization pFabric
    lambdas = [4000, 6000, 10000, 15000, 22500, 37000, 60000]

    FCTs = [[0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]]
    row = 0

    for x in lambdas:
        file = "temp/sppifo/sppifo_evaluation/pFabric/data_mining_workload/"+str(x)+"/TCP/analysis/flow_completion.statistics"
        r = open(file, 'r')
        lines = r.readlines()
        for i, line in enumerate(lines):
            if "geq_1MB_mean_fct_ms" in line:
                FCTs[row][0]=line.split("=")[1].split("\n")[0]
                break
        r.close()

        file = "temp/sppifo/sppifo_evaluation/pFabric/data_mining_workload/"+str(x)+"/DCTCP/analysis/flow_completion.statistics"
        r = open(file, 'r')
        lines = r.readlines()
        for i, line in enumerate(lines):
            if "geq_1MB_mean_fct_ms" in line:
                FCTs[row][1]=line.split("=")[1].split("\n")[0]
                break
        r.close()

        file = "temp/sppifo/sppifo_evaluation/pFabric/data_mining_workload/"+str(x)+"/PIFO/analysis/flow_completion.statistics"
        r = open(file, 'r')
        lines = r.readlines()
        for i, line in enumerate(lines):
            if "geq_1MB_mean_fct_ms" in line:
                FCTs[row][2]=line.split("=")[1].split("\n")[0]
                break
        r.close()

        file = "temp/sppifo/sppifo_evaluation/pFabric/data_mining_workload/"+str(x)+"/SPPIFO/analysis/flow_completion.statistics"
        r = open(file, 'r')
        lines = r.readlines()
        for i, line in enumerate(lines):
            if "geq_1MB_mean_fct_ms" in line:
                FCTs[row][3]=line.split("=")[1].split("\n")[0]
                break
        r.close()

        file = "temp/sppifo/sppifo_evaluation/pFabric/data_mining_workload/"+str(x)+"/XIFO/analysis/flow_completion.statistics"
        r = open(file, 'r')
        lines = r.readlines()
        for i, line in enumerate(lines):
            if "geq_1MB_mean_fct_ms" in line:
                FCTs[row][4]=line.split("=")[1].split("\n")[0]
                break
        r.close()
        row = row + 1

    w = open('projects/sppifo/plots/sppifo_evaluation/pFabric/data_mining_workload/pFabric_geq_1MB_mean_fct_ms.dat', 'w')
    w.write("#      TCP    DCTCP    PIFO    SPPIFO    XIFO\n")
    w.write("4000   %s    %s    %s    %s    %s    \n" % (FCTs[0][0], FCTs[0][1], FCTs[0][2], FCTs[0][3], FCTs[0][4]))
    w.write("6000   %s    %s    %s    %s    %s    \n" % (FCTs[1][0], FCTs[1][1], FCTs[1][2], FCTs[1][3], FCTs[1][4]))
    w.write("10000   %s    %s    %s    %s    %s    \n" % (FCTs[2][0], FCTs[2][1], FCTs[2][2], FCTs[2][3], FCTs[2][4]))
    w.write("15000   %s    %s    %s    %s    %s    \n" % (FCTs[3][0], FCTs[3][1], FCTs[3][2], FCTs[3][3], FCTs[3][4]))
    w.write("22500   %s    %s    %s    %s    %s    \n" % (FCTs[4][0], FCTs[4][1], FCTs[4][2], FCTs[4][3], FCTs[4][4]))
    w.write("37000   %s    %s    %s    %s    %s    \n" % (FCTs[5][0], FCTs[5][1], FCTs[5][2], FCTs[5][3], FCTs[5][4]))
    w.write("60000   %s    %s    %s    %s    %s    \n" % (FCTs[6][0], FCTs[6][1], FCTs[6][2], FCTs[6][3], FCTs[6][4]))
    w.close()

###########################################################################################################################

    # Mean global flow completion time for per service vs. utilization pFabric
    lambdas = [4000, 6000, 10000, 15000, 22500, 37000, 60000]
    number_of_flows = 0

    for value in lambdas:
        number_of_flows += value

    # FCTs is represented by this [CS, Default, EW, GH, MI, QW, RF, RT, SN, TV, YT, YU]
    FCTs = [[0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]]
    
    row = 0

    for x in lambdas:
        file = "temp/sppifo/sppifo_evaluation/pFabric/data_mining_workload/"+str(x)+"/TCP/analysis/flow_completion.statistics"
        r = open(file, 'r')
        lines = r.readlines()
        for line in lines:
            if "service_CS_mean_fct_ns" in line:
                FCTs[0][0] += float(line.split("=")[1].strip())
            if "service_Default_mean_fct_ns" in line:
                FCTs[1][0] += float(line.split("=")[1].strip())
            if "service_EW_mean_fct_ns" in line:
                FCTs[2][0] += float(line.split("=")[1].strip())
            if "service_GH_mean_fct_ns" in line:
                FCTs[3][0] += float(line.split("=")[1].strip())
            if "service_MI_mean_fct_ns" in line:
                FCTs[4][0] += float(line.split("=")[1].strip())
            if "service_QW_mean_fct_ns" in line:
                FCTs[5][0] += float(line.split("=")[1].strip())
            if "service_RF_mean_fct_ns" in line:
                FCTs[6][0] += float(line.split("=")[1].strip())
            if "service_RT_mean_fct_ns" in line:
                FCTs[7][0] += float(line.split("=")[1].strip())
            if "service_SN_mean_fct_ns" in line:
                FCTs[8][0] += float(line.split("=")[1].strip())
            if "service_TV_mean_fct_ns" in line:
                FCTs[9][0] += float(line.split("=")[1].strip())
            if "service_YT_mean_fct_ns" in line:
                FCTs[10][0] += float(line.split("=")[1].strip())
            if "service_YU_mean_fct_ns" in line:
                FCTs[11][0] += float(line.split("=")[1].strip())
        for i in range(0, 12, 1):
            FCTs[i][0] = (FCTs[i][0])/1000000

        r.close()

        file = "temp/sppifo/sppifo_evaluation/pFabric/data_mining_workload/"+str(x)+"/DCTCP/analysis/flow_completion.statistics"
        r = open(file, 'r')
        lines = r.readlines()
        for line in lines:
            if "service_CS_mean_fct_ns" in line:
                FCTs[0][1] += float(line.split("=")[1].strip())
            if "service_Default_mean_fct_ns" in line:
                FCTs[1][1] += float(line.split("=")[1].strip())
            if "service_EW_mean_fct_ns" in line:
                FCTs[2][1] += float(line.split("=")[1].strip())
            if "service_GH_mean_fct_ns" in line:
                FCTs[3][1] += float(line.split("=")[1].strip())
            if "service_MI_mean_fct_ns" in line:
                FCTs[4][1] += float(line.split("=")[1].strip())
            if "service_QW_mean_fct_ns" in line:
                FCTs[5][1] += float(line.split("=")[1].strip())
            if "service_RF_mean_fct_ns" in line:
                FCTs[6][1] += float(line.split("=")[1].strip())
            if "service_RT_mean_fct_ns" in line:
                FCTs[7][1] += float(line.split("=")[1].strip())
            if "service_SN_mean_fct_ns" in line:
                FCTs[8][1] += float(line.split("=")[1].strip())
            if "service_TV_mean_fct_ns" in line:
                FCTs[9][1] += float(line.split("=")[1].strip())
            if "service_YT_mean_fct_ns" in line:
                FCTs[10][1] += float(line.split("=")[1].strip())
            if "service_YU_mean_fct_ns" in line:
                FCTs[11][1] += float(line.split("=")[1].strip())
        
        for i in range(0, 12, 1):
            FCTs[i][1] = (FCTs[i][1])/1000000
        r.close()

        file = "temp/sppifo/sppifo_evaluation/pFabric/data_mining_workload/"+str(x)+"/PIFO/analysis/flow_completion.statistics"
        r = open(file, 'r')
        lines = r.readlines()
        for line in lines:
            if "service_CS_mean_fct_ns" in line:
                FCTs[0][2] += float(line.split("=")[1].strip())
            if "service_Default_mean_fct_ns" in line:
                FCTs[1][2] += float(line.split("=")[1].strip())
            if "service_EW_mean_fct_ns" in line:
                FCTs[2][2] += float(line.split("=")[1].strip())
            if "service_GH_mean_fct_ns" in line:
                FCTs[3][2] += float(line.split("=")[1].strip())
            if "service_MI_mean_fct_ns" in line:
                FCTs[4][2] += float(line.split("=")[1].strip())
            if "service_QW_mean_fct_ns" in line:
                FCTs[5][2] += float(line.split("=")[1].strip())
            if "service_RF_mean_fct_ns" in line:
                FCTs[6][2] += float(line.split("=")[1].strip())
            if "service_RT_mean_fct_ns" in line:
                FCTs[7][2] += float(line.split("=")[1].strip())
            if "service_SN_mean_fct_ns" in line:
                FCTs[8][2] += float(line.split("=")[1].strip())
            if "service_TV_mean_fct_ns" in line:
                FCTs[9][2] += float(line.split("=")[1].strip())
            if "service_YT_mean_fct_ns" in line:
                FCTs[10][2] += float(line.split("=")[1].strip())
            if "service_YU_mean_fct_ns" in line:
                FCTs[11][2] += float(line.split("=")[1].strip())
        
        for i in range(0, 12, 1):
            FCTs[i][2] = (FCTs[i][2])/1000000
        r.close()

        file = "temp/sppifo/sppifo_evaluation/pFabric/data_mining_workload/"+str(x)+"/SPPIFO/analysis/flow_completion.statistics"
        r = open(file, 'r')
        lines = r.readlines()
        for line in lines:
            if "service_CS_mean_fct_ns" in line:
                FCTs[0][3] += float(line.split("=")[1].strip())
            if "service_Default_mean_fct_ns" in line:
                FCTs[1][3] += float(line.split("=")[1].strip())
            if "service_EW_mean_fct_ns" in line:
                FCTs[2][3] += float(line.split("=")[1].strip())
            if "service_GH_mean_fct_ns" in line:
                FCTs[3][3] += float(line.split("=")[1].strip())
            if "service_MI_mean_fct_ns" in line:
                FCTs[4][3] += float(line.split("=")[1].strip())
            if "service_QW_mean_fct_ns" in line:
                FCTs[5][3] += float(line.split("=")[1].strip())
            if "service_RF_mean_fct_ns" in line:
                FCTs[6][3] += float(line.split("=")[1].strip())
            if "service_RT_mean_fct_ns" in line:
                FCTs[7][3] += float(line.split("=")[1].strip())
            if "service_SN_mean_fct_ns" in line:
                FCTs[8][3] += float(line.split("=")[1].strip())
            if "service_TV_mean_fct_ns" in line:
                FCTs[9][3] += float(line.split("=")[1].strip())
            if "service_YT_mean_fct_ns" in line:
                FCTs[10][3] += float(line.split("=")[1].strip())
            if "service_YU_mean_fct_ns" in line:
                FCTs[11][3] += float(line.split("=")[1].strip())
        
        for i in range(0, 12, 1):
            FCTs[i][3] = (FCTs[i][3])/1000000
        r.close()

        file = "temp/sppifo/sppifo_evaluation/pFabric/data_mining_workload/"+str(x)+"/XIFO/analysis/flow_completion.statistics"
        r = open(file, 'r')
        lines = r.readlines()
        for line in lines:
            if "service_CS_mean_fct_ns" in line:
                FCTs[0][4] += float(line.split("=")[1].strip())
            if "service_Default_mean_fct_ns" in line:
                FCTs[1][4] += float(line.split("=")[1].strip())
            if "service_EW_mean_fct_ns" in line:
                FCTs[2][4] += float(line.split("=")[1].strip())
            if "service_GH_mean_fct_ns" in line:
                FCTs[3][4] += float(line.split("=")[1].strip())
            if "service_MI_mean_fct_ns" in line:
                FCTs[4][4] += float(line.split("=")[1].strip())
            if "service_QW_mean_fct_ns" in line:
                FCTs[5][4] += float(line.split("=")[1].strip())
            if "service_RF_mean_fct_ns" in line:
                FCTs[6][4] += float(line.split("=")[1].strip())
            if "service_RT_mean_fct_ns" in line:
                FCTs[7][4] += float(line.split("=")[1].strip())
            if "service_SN_mean_fct_ns" in line:
                FCTs[8][4] += float(line.split("=")[1].strip())
            if "service_TV_mean_fct_ns" in line:
                FCTs[9][4] += float(line.split("=")[1].strip())
            if "service_YT_mean_fct_ns" in line:
                FCTs[10][4] += float(line.split("=")[1].strip())
            if "service_YU_mean_fct_ns" in line:
                FCTs[11][4] += float(line.split("=")[1].strip())
        for i in range(0, 12, 1):
            FCTs[i][4] = (FCTs[i][4])/1000000
        r.close()
        row = row + 1

    w = open('projects/sppifo/plots/sppifo_evaluation/pFabric/data_mining_workload/pFabric_service_based_fct_ms.dat', 'w')
    w.write("#      TCP    DCTCP    PIFO    SPPIFO    XIFO\n")
    w.write("CS   %s    %s    %s    %s    %s    \n" % (FCTs[0][0], FCTs[0][1], FCTs[0][2], FCTs[0][3], FCTs[0][4]))
    w.write("DF   %s    %s    %s    %s    %s    \n" % (FCTs[1][0], FCTs[1][1], FCTs[1][2], FCTs[1][3], FCTs[1][4])) 
    w.write("EW   %s    %s    %s    %s    %s    \n" % (FCTs[2][0], FCTs[2][1], FCTs[2][2], FCTs[2][3], FCTs[2][4]))
    w.write("GH   %s    %s    %s    %s    %s    \n" % (FCTs[3][0], FCTs[3][1], FCTs[3][2], FCTs[3][3], FCTs[3][4]))
    w.write("MI   %s    %s    %s    %s    %s    \n" % (FCTs[4][0], FCTs[4][1], FCTs[4][2], FCTs[4][3], FCTs[4][4]))
    w.write("QW   %s    %s    %s    %s    %s    \n" % (FCTs[5][0], FCTs[5][1], FCTs[5][2], FCTs[5][3], FCTs[5][4]))
    w.write("RF   %s    %s    %s    %s    %s    \n" % (FCTs[6][0], FCTs[6][1], FCTs[6][2], FCTs[6][3], FCTs[6][4]))
    w.write("RT   %s    %s    %s    %s    %s    \n" % (FCTs[7][0], FCTs[7][1], FCTs[7][2], FCTs[7][3], FCTs[7][4]))
    w.write("SN   %s    %s    %s    %s    %s    \n" % (FCTs[8][0], FCTs[8][1], FCTs[8][2], FCTs[8][3], FCTs[8][4]))
    w.write("TV   %s    %s    %s    %s    %s    \n" % (FCTs[9][0], FCTs[9][1], FCTs[9][2], FCTs[9][3], FCTs[9][4]))
    w.write("YT   %s    %s    %s    %s    %s    \n" % (FCTs[10][0], FCTs[10][1], FCTs[10][2], FCTs[10][3], FCTs[10][4]))
    w.write("YU   %s    %s    %s    %s    %s    \n" % (FCTs[11][0], FCTs[11][1], FCTs[11][2], FCTs[11][3], FCTs[11][4]))
    w.close()