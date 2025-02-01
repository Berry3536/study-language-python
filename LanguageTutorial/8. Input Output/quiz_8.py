for week in range(1, 51):
    with open("{0}주차.txt".format(week), "w", encoding="utf8") as weeklyReport_file:
        weeklyReport_file.write(" - {0} 주차 주간보고 - \n 부서 :\n 이름 :\n 업무 요약 : \n".format(week))