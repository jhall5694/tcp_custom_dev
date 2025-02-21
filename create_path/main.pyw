import tkinter as tk
import pyperclip
import sys


btn_index = 0
ary_path = ''
ary_path_str = ''
ary_path_str_base = ''
final_path_str = ''

ary_menu =  \
["Settings", \
  ["My Dashboard", \
  "Hours", \
    ["Individual Hours", \
    "Group Hours", \
    "Mass Hours", \
    "Covered Hours", \
    "Period Export", \
    "Time Sheets"
    ], \
  "Schedules", \
    ["Employee", \
    "Daily", \
    "Weekly", \
    "Recurring", \
    "Template", \
    "Global Scheduler", \
    "Staffing Requirements", \
    "Shift Assignments", \
      ["Shift Roster", \
      "Shift Calendar"
      ], \
    "Shift Board", \
      ["Swaps", \
      "Drops", \
      "Opens"
      ]
    ], \
  "Employee", \
    ["Employee Profiles", \
      ["Information", \
        ["Personal", \
          ["ID", \
          "First name", \
          "Last name", \
          "Address", \
          "City", \
          "State", \
          "Zip", \
          "Gender", \
          "DOB", \
          "SSN", \
          "Language", \
          "Cell", \
          "Phone", \
          "Office Phone", \
          "ext", \
          "Email", \
          "SMS Address" \
          ], \
        "Company", \
          ["Override role settings", \
          "Role ID", \
          "Description", \
          "Classification", \
          "Department", \
          "Default Location", \
          "Schedule Group", \
          "None", \
          "Full time", \
          "Part time", \
          "Seniority Date", \
          "Hire date", \
          "Export code", \
          "Import ID", \
          "Termination", \
          "Suspended" \
          ], \
        "Role History", \
        "Other", \
          ["Network ID", \
          "LDAP User Name", \
          "Badge", \
          "PIN Status", \
          "PIN is not set", \
          "New PIN", \
          "Re-Enter PIN", \
          "Password Status", \
          "Password is not blank", \
          "New Password", \
          "Re-Enter Password", \
          "Employee must change password every", \
          "Days", \
          "SubSearch Plus account email", \
          "NA" \
          ], \
        "Qualifications", \
          ["Active only" \
          ] \
        ], \
      "Jobs", \
        ["Work Profile", \
          ["Active only" \
          ], \
        "Job Code", \
          ["Leave", \
          "Non-Clockable", \
          "Active only" \
          ], \
        "Default", \
          ["Override role settings", \
          "Default pay rate", \
          "0.0000", \
          "Currency format", \
          "Default Job Code", \
          "Never", \
          "Default job code", \
          "Scheduled job code", \
          "Scheduled job code, use default if not scheduled", \
          "Default Cost Code", \
          "Never", \
          "Default cost code", \
          "Scheduled cost code", \
          "Scheduled cost code, use default if not scheduled" \
          ], \
        "Cost Code Groups", \
          ["Active only", \
          "No records found" \
          ], \
        "Rate Change History", \
        "Currency Format Change History", \
          ["Download", \
          "No records found" \
          ] \
        ], \
      "Overtime", \
        ["Rules", \
          ["Override role settings", \
          "Employee also earns a salaried amount of", \
          "per year", \
          "Ignore regular hours for this employee", \
          "Overtime #1 after", \
          "hours:minutes per week", \
          "Overtime #2 after", \
          "hours:minutes per week", \
          "Overtime 1", \
          "Overtime 2" \
          ], \
        "Advanced", \
          ["Override role settings", \
          "No special action for these days", \
          "Override overtime settings for these days", \
          "Overtime #1 after", \
          "hours in the day", \
          "Overtime #2 after", \
          "hours in the day", \
          "Pay a shift premium of", \
          "dollars per hour", \
          "Must have worked at least", \
          "counted hours in overtime period", \
          "No special action for these days", \
          "Override overtime settings for these days", \
          "Overtime #1 after", \
          "hours in the day", \
          "Overtime #2 after", \
          "hours in the day", \
          "Pay a shift premium of", \
          "dollars per hour", \
          "Must have worked at least", \
          "counted hours in overtime period", \
          "No special action for these days", \
          "Override overtime settings for these days", \
          "Overtime #1 after", \
          "hours in the day", \
          "Overtime #2 after", \
          "hours in the day", \
          "Pay a shift premium of", \
          "dollars per hour", \
          "Must have worked at least", \
          "counted hours in overtime period" \
          ], \
        "Comp Time", \
          ["Override role settings", \
          "No comp time", \
          "Comp time at overtime", \
          "Comp time after", \
          "per day", \
          "per period", \
          "Comp time at daily contracted hours", \
          "Comp time at overtime period contracted hours" \
          ], \
        "Contracts First", \
        "Paid Break Limit", \
          ["Override company settings", \
          "Group 1", \
          "Group 2", \
          "Group 3", \
          "Group 4", \
          "No records found", \
          "break_15_min", \
          "Lunch_30_min", \
          "break_30_min", \
          "break_15_min", \
          "Break5" \
          ], \
        "Weighted Overtime", \
          ["Override company settings", \
          "Weighted Base Rate: All WagesAll Hours OTRate=RegRate x Factor", \
          "Weighted Overtime Rate: RegRate=No Change OTRate=RegRate+(Weighted Factor)", \
          "Weighted Overtime Rate: RegRate=No Change OTRate=Weighted Base x Factor", \
          "Redistribute overtime hours to each job code worked", \
          "For base rate calculation wages are determined by calculating the sum of all unique regular rates times the number of hours worked in that rate", \
          "Calculate on a weekly basis even if employee is bi-weekly or quad-weekly", \
          "Process calculations when exporting data", \
          "Process calculations when generating reports", \
          "Include rate of pay when determining job code groups for redistribution of hours", \
          "Distribute overtime for shift segments that are forced to overtime", \
          "Distribute overtime to shift segments that do not earn overtime", \
          "Distribute overtime to end of distribution period first", \
          "Round weighted rate up to the nearest cent" \
          ] \
        ], \
      "Payroll", \
        ["Cumulative", \
          ["to", \
          "Start date", \
          "Stop date", \
          "Period", \
          "Download" \
          ], \
        "Shift Differential", \
          ["Override role settings", \
          "Shift schedule", \
          "Override company settings", \
          "Include shift differential premium in base rate when calculating overtime" \
          ], \
        "Workweek Finalizer", \
          ["Override role settings", \
          "Enabled", \
          "Override company settings", \
          "Minimum hours", \
          "Default hours", \
          "Job Code" \
          ], \
        "Benefit Status", \
          ["Override role settings", \
          "Measurement period group", \
          "Break period group", \
          "Measurement start" \
          ], \
        "Split By Percentage", \
          ["Enabled", \
          "No records found" \
          ], \
        "Pay Progressions", \
          ["Active only" \
          ], \
        "Budgets", \
          ["Active only" \
          ] \
        ], \
       "Access", \
        ["Access", \
          ["Override role settings", \
          "Manager" \
          ], \
        "Clock Configurations", \
          ["Override role settings", \
          "WebClock", \
          "MobileClock", \
          "Telephone Clock" \
          ], \
        "Mobile Devices", \
        "Provisioning", \
          ["Override role settings", \
          "Clockable", \
          "862 provisions are in use", \
          "Non-Clockable", \
          "0 provisions are in use", \
          "Advanced Scheduler", \
          "0 provisions are in use" \
          ], \
        "Single Sign On", \
          ["Override role settings", \
          "Require SSO for WebClock" \
          ], \
        "Multifactor Authentication" \
        ], \
      ],
    "Employee Roles", \
      ["Information", \
        ["Company", \
          ["Override role settings", \
          "Role ID", \
          "Description", \
          "Classification", \
          "Department", \
          "Default Location", \
          "Schedule Group", \
          "None", \
          "Full time", \
          "Part time" \
          ], \
        "Qualifications", \
          ["Active only" \
          ] \
        ], \
     "Jobs", \
        ["Job Code", \
          ["Leave", \
          "Active only", \
          "Assignment clears non-role job codes", \
          "Assignment resets role job codes", \
          "Unassignment clears role job codes" \
          ], \
        "Default", \
          ["Override role settings", \
          "Default pay rate", \
          "0.0000", \
          "Currency format", \
          "Default Job Code", \
          "Never", \
          "Default job code", \
          "Scheduled job code", \
          "Scheduled job code, use default if not scheduled", \
          "Default Cost Code", \
          "Never", \
          "Default cost code", \
          "Scheduled cost code", \
          "Scheduled cost code, use default if not scheduled" \
          ], \
        "Cost Code Groups", \
          ["Active only", \
          "No records found", \
          "Assignment clears non-role cost code groups", \
          "Assignment resets role cost code groups", \
          "Unassignment clears role cost code groups" \
          ], \
        "Rate Change History", \
          ["Download", \
          "No records found" \
          ], \
        "Currency Format Change History", \
          ["Download", \
          "No records found" \
          ] \
        ], \
      ], \
    "Dashboard Templates", \
    "Global Modification", \
    "Employee Messaging", \
    "Pay Progressions", \
    "Employee Recovery"
    ], \
  "Reports", \
    ["Period Reports", \
    "Scheduler Reports", \
    "Analytics"
    ], \
  "Tools", \
    ["Import", \
    "Export", \
    "Employee Status", \
    "Requests", \
      ["Request Manager", \
      "Substitute Assignment Manager", \
      "Leave Bid Manager", \
      "FMLA Case Manager"
      ], \
    "Labor Analytics", \
    "Labor Cost", \
      ["Worked", \
      "Schedule"
      ], \
    "Documents", \
      ["Document Categories", \
      "General Documents"
      ], \
    "QR Code Generator", \
    "Other Tools", \
      ["Attendance Monitor", \
      "Audit Log", \
      "Notifications", \
      "Unresolved Punches", \
      "Data Purge", \
      "Calculator"
      ]
    ], \
  "Configuration", \
    ["Users", \
      ["User Profiles", \
        ["Permissions",
          ["Access Rights", \
            ["System Wide", \
              ["User can view/edit birthdates", \
              "User can view/edit cell phone numbers", \
              "User can view/edit employee network id", \
              "User can view/edit employee rates and wages", \
              "User can view/edit employee social security numbers", \
              "User can view/edit employee badge number", \
              "User can view/edit employee personal identification numbers", \
              "User can view/edit private custom fields", \
              "User can view/edit employee photos", \
              "User can view/edit employee language", \
              "User can view/edit user profile language selection", \
              "User can view job classes", \
              "User can view release notes", \
              "User can submit feedback", \
              "User can add open shifts", \
              "User can view/edit employee passwords feature", \
              "User Can View/Edit Employee Import ID", \
              "User Can View/Edit Job Code Import ID" \
              ],
            "Exceptions", \
              ["Schedule", \
                ["Absent", \
                  ["View exception", \
                  "Approve/unapprove exception", \
                  "Approve/unapprove exception in own records" \
                  ],
                "Early/Late clock in", \
                  ["View exception", \
                  "Approve/unapprove exception", \
                  "Approve/unapprove exception in own records" \
                  ],
                "Early/Late clock out", \
                  ["View exception", \
                  "Approve/unapprove exception", \
                  "Approve/unapprove exception in own records" \
                  ],
                "Job Code Day of Week", \
                  ["View exception", \
                  "Approve/unapprove exception", \
                  "Approve/unapprove exception in own records" \
                  ],
                "Tardy 1", \
                  ["View exception", \
                  "Approve/unapprove exception", \
                  "Approve/unapprove exception in own records" \
                  ],
                "Tardy 2", \
                  ["View exception", \
                  "Approve/unapprove exception", \
                  "Approve/unapprove exception in own records" \
                  ],
                "Unscheduled Work", \
                  ["View exception", \
                  "Approve/unapprove exception", \
                  "Approve/unapprove exception in own records" \
                  ], \
                ],
              "Shift", \
                ["Active Period", \
                  ["View exception", \
                  "Approve/unapprove exception", \
                  "Approve/unapprove exception in own records" \
                  ],
                "Comp Time Overtime", \
                  ["View exception", \
                  "Approve/unapprove exception", \
                  "Approve/unapprove exception in own records" \
                  ],
                "Comp Time Regular", \
                  ["View exception", \
                  "Approve/unapprove exception", \
                  "Approve/unapprove exception in own records" \
                  ],
                "Conflicting shift", \
                  ["View exception", \
                  "Approve/unapprove exception", \
                  "Approve/unapprove exception in own records" \
                  ],
                "Geofencing", \
                  ["View exception", \
                  "Approve/unapprove exception", \
                  "Approve/unapprove exception in own records" \
                  ],
                "Holiday", \
                  ["View exception", \
                  "Approve/unapprove exception", \
                  "Approve/unapprove exception in own records" \
                  ],
                "Long break", \
                  ["View exception", \
                  "Approve/unapprove exception", \
                  "Approve/unapprove exception in own records" \
                  ],
                "Long week", \
                  ["View exception", \
                  "Approve/unapprove exception", \
                  "Approve/unapprove exception in own records" \
                  ],
                "Long shift", \
                  ["View exception", \
                  "Approve/unapprove exception", \
                  "Approve/unapprove exception in own records" \
                  ],
                "Missed break", \
                  ["View exception", \
                  "Approve/unapprove exception", \
                  "Approve/unapprove exception in own records" \
                  ],
                "First Meal Break", \
                  ["View exception", \
                  "Approve/unapprove exception", \
                  "Approve/unapprove exception in own records" \
                  ],
                "Second Meal Break", \
                  ["View exception", \
                  "Approve/unapprove exception", \
                  "Approve/unapprove exception in own records" \
                  ],
                "Negative accrual balance", \
                  ["View exception", \
                  "Approve/unapprove exception", \
                  "Approve/unapprove exception in own records" \
                  ],
                "Missed punch", \
                  ["View exception", \
                  "Approve/unapprove exception", \
                  "Approve/unapprove exception in own records" \
                  ],
                "Over Budget", \
                  ["View exception", \
                  "Approve/unapprove exception", \
                  "Approve/unapprove exception in own records" \
                  ],
                "Overtime", \
                  ["View exception", \
                  "Approve/unapprove exception", \
                  "Approve/unapprove exception in own records" \
                  ],
                "Seventh consecutive day worked", \
                  ["View exception", \
                  "Approve/unapprove exception", \
                  "Approve/unapprove exception in own records" \
                  ],
                "Short break", \
                  ["View exception", \
                  "Approve/unapprove exception", \
                  "Approve/unapprove exception in own records" \
                  ],
                "Short shift gap", \
                  ["View exception", \
                  "Approve/unapprove exception", \
                  "Approve/unapprove exception in own records" \
                  ],
                "Sixth consecutive day worked", \
                  ["View exception", \
                  "Approve/unapprove exception", \
                  "Approve/unapprove exception in own records" \
                  ], \
                ],
              "Approvals", \
                ["Employee approval", \
                  ["View", \
                  "Approve/unapprove", \
                  "Approve/unapprove in own records" \
                  ],
                "Manager approval", \
                  ["View", \
                  "Approve/unapprove", \
                  "Approve/unapprove in own records" \
                  ],
                "Other approval", \
                  ["View", \
                  "Approve/unapprove", \
                  "Approve/unapprove in own records" \
                  ], \
                ], \
              ],
            "Job Code Access Overrides", \
              ["Hours", \
                ["Add a note to hours in an inaccessible job code", \
                "Add hours for an inaccessible job code", \
                "Delete hours for an inaccessible job code", \
                "Edit hours for an inaccessible job code", \
                "View description of an inaccessible job code" \
                ],
              "Requests", \
                ["Add a request in an inaccessible job code", \
                "Approve/Deny requests in an inaccessible job code", \
                "Delete a request for an inaccessible job code", \
                "Edit a request in an inaccessible job code" \
                ],
              "Schedules", \
                ["Add a schedule segment in an inaccessible job code", \
                "Delete a schedule segment in an inaccessible job code", \
                "Edit a schedule segment in an inaccessible job code" \
                ],
              "Reports", \
                ["View description of an inaccessible job code" \
                ],
              "Exceptions(Requires regular exception access)", \
                ["Schedule", \
                  ["Absent", \
                    ["View", \
                    "Approve/unapprove exception in an inaccessible job code" \
                    ],
                  "Early/Late clock in", \
                    ["View", \
                    "Approve/unapprove exception in an inaccessible job code" \
                    ],
                  "Early/Late clock out", \
                    ["View", \
                    "Approve/unapprove exception in an inaccessible job code" \
                    ],
                  "Job Code Day of Week", \
                    ["View", \
                    "Approve/unapprove exception in an inaccessible job code" \
                    ],
                  "Tardy 1", \
                    ["View", \
                    "Approve/unapprove exception in an inaccessible job code" \
                    ],
                  "Tardy 2", \
                    ["View", \
                    "Approve/unapprove exception in an inaccessible job code" \
                    ],
                  "Unscheduled Work", \
                    ["View", \
                    "Approve/unapprove exception in an inaccessible job code" \
                    ], \
                  ],
                "Shift", \
                  ["Active Period", \
                    ["View", \
                    "Approve/unapprove exception in an inaccessible job code" \
                    ],
                  "Comp Time Overtime", \
                    ["View", \
                    "Approve/unapprove exception in an inaccessible job code" \
                    ],
                  "Comp Time Regular", \
                    ["View", \
                    "Approve/unapprove exception in an inaccessible job code" \
                    ],
                  "Conflicting shift", \
                    ["View", \
                    "Approve/unapprove exception in an inaccessible job code" \
                    ],
                  "Geofencing", \
                    ["View", \
                    "Approve/unapprove exception in an inaccessible job code" \
                    ],
                  "Holiday", \
                    ["View", \
                    "Approve/unapprove exception in an inaccessible job code" \
                    ],
                  "Long break", \
                    ["View", \
                    "Approve/unapprove exception in an inaccessible job code" \
                    ],
                  "Long week", \
                    ["View", \
                    "Approve/unapprove exception in an inaccessible job code" \
                    ],
                  "Long shift", \
                    ["View", \
                    "Approve/unapprove exception in an inaccessible job code" \
                    ],
                  "Missed break", \
                    ["View", \
                    "Approve/unapprove exception in an inaccessible job code" \
                    ],
                  "Missed First Meal Break", \
                    ["View", \
                    "Approve/unapprove exception in an inaccessible job code" \
                    ],
                  "Missed Second Meal Break", \
                    ["View", \
                    "Approve/unapprove exception in an inaccessible job code" \
                    ],
                  "Missed punch", \
                    ["View", \
                    "Approve/unapprove exception in an inaccessible job code" \
                    ],
                  "Negative accrual balance", \
                    ["View", \
                    "Approve/unapprove exception in an inaccessible job code" \
                    ],
                  "Seventh consecutive day worked", \
                    ["View", \
                    "Approve/unapprove exception in an inaccessible job code" \
                    ],
                  "Short break", \
                    ["View", \
                    "Approve/unapprove exception in an inaccessible job code" \
                    ],
                  "Short shift gap", \
                    ["View", \
                    "Approve/unapprove exception in an inaccessible job code" \
                    ],
                  "Sixth consecutive day worked", \
                    ["View", \
                    "Approve/unapprove exception in an inaccessible job code" \
                    ],
                  "Over Budget", \
                    ["View", \
                    "Approve/unapprove exception in an inaccessible job code" \
                    ],
                  "Overtime", \
                    ["View", \
                    "Approve/unapprove exception in an inaccessible job code" \
                    ], \
                  ],
                "Approval", \
                  ["Employee approval", \
                    ["View", \
                    "Approve/unapprove exception in an inaccessible job code" \
                    ],
                  "Manager approval", \
                    ["View", \
                    "Approve/unapprove exception in an inaccessible job code" \
                    ],
                  "Other approval", \
                    ["View", \
                    "Approve/unapprove exception in an inaccessible job code" \
                    ], \
                  ], \
                ], \
              ],
            "Manager", \
              ["Edit his/her own dashboard", \
              "View dashboard", \
              "Clair On-Demand Pay", \
              "Hours", \
                ["Individual Hours", \
                  ["Add hours", \
                  "View hours", \
                  "Schedule", \
                  "Accruals", \
                    ["Add accruals", \
                    "Delete accruals", \
                    "Edit accruals", \
                    "View accruals" \
                    ], \
                  ],
                "Group Hours", \
                  ["Add hours", \
                  "View hours" \
                  ],
                "Covered Employee Hours", \
                  ["View hours" \
                  ],
                "Mass Hours Change", \
                  ["Add", \
                  "Delete", \
                  "Edit", \
                  "Processing" \
                  ],
                "Period Export", \
                  ["Create templates", \
                  "Delete common saved templates", \
                  "Delete his/her own saved templates", \
                  "Edit common saved templates", \
                  "Edit his/her own saved templates", \
                  "Access", \
                  "Automation", \
                    ["Edit", \
                    "Edit export automation run as User" \
                    ], \
                  ],
                "Time Sheets", \
                  ["Add Time Sheets" \
                  ],
                "Segment Options", \
                  ["Access custom fields when adding", \
                  "Access extra options when adding", \
                  "Add breaks (requires change break type)", \
                  "Add Hours as Time Sheet", \
                  "Add hours in closed weeks", \
                  "Add hours in locked period", \
                  "Delete hours", \
                  "Delete hours in closed weeks", \
                  "Delete hours in locked period", \
                  "Edit existing hours", \
                  "Edit hours that result in negative accrual balances", \
                  "Allow editing hours over usage cap", \
                  "Edit hours in closed weeks", \
                  "Edit hours in locked period", \
                  "Resolve Period", \
                  "Split shifts", \
                  "View segment photo", \
                  "View Location", \
                  "View hours in closed weeks", \
                  "View temperature score in segment", \
                  "Edit Details", \
                    ["Allow entering blank employee work profile", \
                    "Change actual times", \
                    "Change break type", \
                    "Change comp time", \
                    "Change custom fields", \
                    "Change extra information", \
                    "Change FMLA settings", \
                    "Change job code", \
                    "Change labor code", \
                    "Change labor standards", \
                    "Change missed in/out status", \
                    "Change rate", \
                    "Change substitute ID", \
                    "Change time/date in", \
                    "Change time/date out", \
                    "Change time sheet amount", \
                    "Change Time Sheet Flag", \
                    "Change tracked fields", \
                    "Edit work profile" \
                    ],
                  "Shift Notes", \
                    ["Add", \
                    "View", \
                    "Delete", \
                      ["Notes entered by employee", \
                      "Notes entered by other users", \
                      "Notes entered by self" \
                      ],
                    "Edit", \
                      ["Notes entered by employee", \
                      "Notes entered by other users", \
                      "Notes entered by self" \
                      ], \
                    ],
                  "User's Own Hours (Employee must be set in user information)", \
                    ["Add hours to user's own record", \
                    "Delete user's own records", \
                    "Edit user's own records" \
                    ], \
                  ],
                "Processing", \
                  ["Finalize Workweeks", \
                  "Process Contracts", \
                  "Process Persisted Calculations", \
                  "Process Shift Differential" \
                  ],
                "Occurrence Ledger", \
                  ["View", \
                  "Add", \
                  "Delete", \
                  "Edit" \
                  ], \
                ],
              "Schedules", \
                ["Employee Schedule", \
                  ["Add schedules", \
                  "Delete schedules", \
                  "Edit recurring schedule assignments", \
                  "Edit schedules", \
                  "View" \
                  ],
                "Daily Overall Schedule", \
                  ["View" \
                  ],
                "Weekly Overall Schedule", \
                  ["View" \
                  ],
                "Manage Recurring Schedules", \
                  ["Add and Edit", \
                  "Delete", \
                  "Edit", \
                  "View" \
                  ],
                "Manage Schedule Templates", \
                  ["Add schedule templates", \
                  "Delete schedule templates", \
                  "Edit schedule templates", \
                  "View schedule templates" \
                  ],
                "Global Schedules", \
                  ["Apply schedules", \
                  "Copy schedules", \
                  "Delete schedules", \
                  "Modify schedules", \
                  "Recurring Schedules", \
                  "Reset recurring schedule overrides", \
                  "Transfer Job Code information" \
                  ],
                "Staffing Requirements", \
                  ["Add", \
                  "Assign", \
                  "Delete", \
                  "Edit", \
                  "View" \
                  ],
                "Shift Assignments", \
                  ["Edit", \
                  "View Shift Calendar", \
                  "View Shift Roster", \
                  "Delete" \
                  ],
                "Shift Board", \
                  ["View Swaps", \
                    ["User can view swaps", \
                    "User can grant employee approval", \
                    "User can approve swap requests", \
                    "User can approve swap requests exceeding swap limit threshold", \
                    "User can approve swap requests involving employees they cannot access", \
                    "User can approve swap requests involving master shifts and master schedules they cannot access", \
                    "User can delete swap requests", \
                    "User can change how swapped hours are paid", \
                    "User can edit shifts in a swap request", \
                    "Swap Notes", \
                      ["Add", \
                      "Delete", \
                      "Edit", \
                      "View" \
                      ], \
                    ],
                  "View Drops", \
                    ["User can view drops", \
                    "User can approve drops", \
                    "User can approve and assign", \
                    "User can approve and offer", \
                    "User can delete drops" \
                    ],
                  "View Opens", \
                    ["User can view assigned offers", \
                    "User can view offers", \
                    "User can view opens", \
                    "User can assign offered shifts", \
                    "User can assign open shifts", \
                    "User can edit open shifts", \
                    "User can delete open shifts", \
                    "User can offer open shifts", \
                    "User can reoffer shifts", \
                    "User can unassign shifts" \
                    ], \
                  ],
                "Allowed Schedule Segment Types", \
                  ["Regular", \
                  "Off", \
                  "Open", \
                  "On-Call", \
                  "Unavailable" \
                  ],
                "Offers", \
                  ["Mark interested on behalf of employee", \
                  "Mark uninterested on behalf of employee", \
                  "Skip employee", \
                  "Notes", \
                    ["Add", \
                    "View", \
                    "Delete", \
                      ["Delete notes entered by self", \
                      "Delete notes entered by other users" \
                      ],
                    "Edit", \
                      ["Edit notes entered by self", \
                      "Edit notes entered by other users" \
                      ], \
                    ], \
                  ], \
                ],
              "Employee", \
                ["Employee Profiles", \
                  ["Add Employee", \
                  "Add over limit", \
                  "Delete employee", \
                  "Edit role assignment", \
                  "Information", \
                    ["Personal", \
                      ["Edit", \
                      "View", \
                      "Change photo" \
                      ],
                    "Company", \
                      ["Edit", \
                      "View" \
                      ],
                    "Other", \
                      ["Edit", \
                      "View" \
                      ],
                    "Qualification", \
                      ["Add", \
                      "Delete", \
                      "Edit", \
                      "View" \
                      ], \
                    ],
                  "Jobs", \
                    ["Work Profile", \
                      ["Assign work profile", \
                      "Edit work profile", \
                      "Unassign work profile", \
                      "View" \
                      ],
                    "Job Code", \
                      ["Assign job code", \
                      "Edit job code", \
                      "Unassign job code", \
                      "View" \
                      ],
                    "Default", \
                      ["Edit", \
                      "View" \
                      ],
                    "Currency Format Change History", \
                      ["View" \
                      ], \
                    ],
                  "Occurrences", \
                    ["Occurrence Rules", \
                      ["Edit", \
                      "View" \
                      ],
                    "Occurrences Drop Off", \
                      ["Edit", \
                      "View" \
                      ],
                    "Occurrence Ledger", \
                      ["View", \
                      "Add", \
                      "Delete", \
                      "Edit" \
                      ],
                    "Notification Thresholds", \
                      ["Add", \
                      "Delete", \
                      "Edit", \
                      "View" \
                      ], \
                    ],
                  "Overtime", \
                    ["Rules", \
                      ["Edit", \
                      "View" \
                      ],
                    "Calculation Modules", \
                      ["Edit", \
                      "View" \
                      ],
                    "Advanced", \
                      ["Edit", \
                      "View" \
                      ],
                    "Comp Time", \
                      ["Edit", \
                      "View" \
                      ], \
                    ],
                  "Hours", \
                    ["Rounding", \
                      ["Edit", \
                      "View" \
                      ],
                    "Schedule", \
                      ["Edit", \
                      "View" \
                      ],
                    "Automatic Break", \
                      ["Assign automatic break", \
                      "Edit automatic break", \
                      "Unassign automatic break", \
                      "View" \
                      ],
                    "Time Zone", \
                      ["Edit", \
                      "View" \
                      ],
                    "Locked Period", \
                      ["Edit", \
                      "View" \
                      ],
                    "Workday Adjustment", \
                      ["Edit", \
                      "View" \
                      ],
                    "Work Week Settings", \
                      ["Edit", \
                      "View" \
                      ],
                    "Advanced Scheduler", \
                      ["Edit", \
                      "View" \
                      ],
                    "Swap Limits", \
                      ["Add", \
                      "Delete" \
                      ],
                    "Hours Calculation Priority Groups", \
                      ["View", \
                      "Edit" \
                      ], \
                    ],
                  "Leave", \
                    ["Request Template", \
                      ["Edit", \
                      "View" \
                      ],
                    "Request", \
                      ["Edit", \
                      "View" \
                      ],
                    "Accrual Bank", \
                      ["Assign accrual bank", \
                      "Edit accrual bank", \
                      "Unassign accrual bank", \
                      "View", \
                      "Accruals", \
                        ["Add accruals", \
                        "Edit accruals", \
                        "Remove accruals", \
                        "Transfer accruals" \
                        ], \
                      ],
                    "Holidays", \
                      ["Edit", \
                      "View" \
                      ],
                    "Leave Groups", \
                      ["Edit", \
                      "View" \
                      ],
                    "Leave Calendars", \
                      ["Edit", \
                      "View" \
                      ],
                    "Substitute Assignment Templates", \
                      ["Edit", \
                      "View" \
                      ], \
                    ],
                  "Payroll", \
                    ["Cumulative", \
                      ["View" \
                      ],
                    "Shift Differential", \
                      ["Edit", \
                      "View" \
                      ],
                    "Workweek Finalizer", \
                      ["Edit", \
                      "View" \
                      ],
                    "Benefit Status", \
                      ["Edit", \
                      "View" \
                      ],
                    "Split By Percentage", \
                      ["Edit", \
                      "View" \
                      ],
                    "Pay Progression", \
                      ["Edit", \
                      "View", \
                      "Ledger", \
                        ["Add", \
                        "Delete", \
                        "Edit", \
                        "View" \
                        ], \
                      ],
                    "Budgets", \
                      ["Edit", \
                      "View" \
                      ], \
                    ],
                  "Access", \
                    ["Access", \
                      ["Assign access", \
                      "Assign manager", \
                      "Edit employee user", \
                      "Unassign access", \
                      "View" \
                      ],
                    "Clock Configuration", \
                      ["Edit", \
                      "View" \
                      ],
                    "Device Management", \
                      ["Edit", \
                      "View" \
                      ],
                    "Provisioning", \
                      ["View", \
                      "Edit", \
                      "Warn if a user is going over their allotted amount of the provision", \
                        ["Clockable", \
                        "Non-Clockable", \
                        "Sub/Temp", \
                        "Advanced Scheduler", \
                        "SubSearch Plus (Sub)", \
                        "SubSearch Plus", \
                        "PointSystem Plus" \
                        ], \
                      ],
                    "Single Sign On", \
                      ["Edit", \
                      "View" \
                      ],
                    "Locations", \
                      ["Edit", \
                      "View" \
                      ],
                    "Mobile App Access", \
                      ["Edit", \
                      "View" \
                      ], \
                    ],
                  "Exceptions", \
                    ["Approvals", \
                      ["Edit", \
                      "View" \
                      ],
                    "Shift", \
                      ["Edit", \
                      "View" \
                      ],
                    "Schedule", \
                      ["Edit", \
                      "View" \
                      ], \
                    ],
                  "Personnel", \
                    ["Note", \
                      ["Add note", \
                      "Edit note", \
                      "Remove note", \
                      "View" \
                      ],
                    "Review", \
                      ["Add review", \
                      "Edit review", \
                      "Remove review", \
                      "View" \
                      ],
                    "Attestations", \
                      ["Assign", \
                      "Edit", \
                      "Revoke", \
                      "Unassign", \
                      "View" \
                      ], \
                    ],
                  "Custom Field", \
                    ["Edit custom fields", \
                    "View" \
                    ],
                  "Contracts", \
                    ["Edit", \
                    "View", \
                    "Period Processing Edit", \
                    "Period Processing View" \
                    ],
                  "FMLA", \
                    ["Edit", \
                    "View" \
                    ],
                  "Documents", \
                    ["Add", \
                    "Edit", \
                    "Delete", \
                    "Download", \
                    "View" \
                    ], \
                  ],
                "Employee Roles", \
                  ["Add", \
                  "Delete", \
                  "Edit", \
                  "View" \
                  ],
                "Employee Dashboard Templates", \
                  ["Add", \
                  "Delete", \
                  "Edit", \
                  "View" \
                  ],
                "Global Modification", \
                  ["Option is visible to user", \
                  "Clear employee messages", \
                  "Process Accruals" \
                  ],
                "Employee Messaging", \
                  ["Compose Message", \
                  "Send Company wide bulletin", \
                  "Delete other's employee messages", \
                  "Expire other's employee messages", \
                  "Delete other's Company Bulletins", \
                  "Expire other's Company Bulletins", \
                  "View message history", \
                  "View other's message history", \
                  "View other's Company Bulletins history" \
                  ],
                "Pay Progression", \
                  ["Add", \
                  "Delete", \
                  "Edit", \
                  "View" \
                  ],
                "Employee Recovery", \
                  ["Edit", \
                  "View" \
                  ], \
                ],
              "Reports", \
                ["View Modular Reports", \
                "Period Reports", \
                  ["Can make report public", \
                  "Change report options", \
                  "Change report settings", \
                  "Create saved reports", \
                  "Delete common saved reports", \
                  "Delete his/her own saved reports", \
                  "Edit common saved reports", \
                  "Edit his/her own saved reports", \
                  "Automation", \
                    ["Edit", \
                    "Edit report automation run as User" \
                    ],
                  "Payroll Reports", \
                    ["Approaching Exception", \
                    "Approaching Overtime", \
                    "Complete Payroll", \
                    "Comp Time Detail", \
                    "Day Breakdown", \
                    "Estimated Wages", \
                    "Exception Summary", \
                    "Employees Without Exceptions", \
                    "Individual Exception", \
                    "Individual Job", \
                    "Individual Tracked Field Summary", \
                    "Overtime", \
                    "Pay Progression Status", \
                    "Payroll Detail", \
                    "Payroll Summary", \
                    "Shift Note", \
                    "Substitute Work Day", \
                    "Supplemental Pay", \
                    "Weekly Punch", \
                    "Weekly Summary", \
                    "Bill Rate" \
                    ],
                  "Job Code Reports", \
                    ["Employee Job Codes", \
                    "Job Code Analysis Detail", \
                    "Job Code Analysis Summary", \
                    "Job Code Group Detail", \
                    "Job Code Group Summary", \
                    "Job Code Overtime", \
                    "Job Code Split", \
                    "Selected Job Code" \
                    ],
                  "Scheduler Reports", \
                    ["Schedule Variance", \
                    "Schedule vs. Actual", \
                    "Schedule vs. Actual Breakdown" \
                    ],
                  "Period Reports", \
                    ["Period (Detail)", \
                    "Period (Summary)", \
                    "Period Variance", \
                    "Budget Comparison", \
                    "Employee Occurrence Detail", \
                    "Individual Occurrence Detail" \
                    ],
                  "Cost Code Reports", \
                    ["Cost Code Summary" \
                    ],
                  "Accrual Reports", \
                    ["Employee Accrual Bank", \
                    "Accrual Usage", \
                    "Future Cost of Accruals", \
                    "Period Accrual" \
                    ],
                  "Miscellaneous Reports", \
                    ["Substitute", \
                    "Employee Information", \
                    "Anniversary", \
                    "Birthday", \
                    "Break Totals", \
                    "Digital Output Access", \
                    "Punch Location", \
                    "Recorded Absent and Tardy (Legacy)", \
                    "Requests", \
                    "Scheduled Reviews", \
                    "Time Coverage", \
                    "User Audit Security" \
                    ],
                  "Contract Reports", \
                    ["Contract Details", \
                    "Contract Variance", \
                    "Estimated Wages for Contract Variance", \
                    "Contract Job Code Association" \
                    ],
                  "Benefit Status Reports", \
                    ["Measurement Period" \
                    ],
                  "SubSearch Reports", \
                    ["Schedule Variance", \
                    "Substitute Coverage", \
                    "Substitute Time Detail" \
                    ],
                  "FMLA Reports", \
                    ["FMLA Case Summary", \
                    "FMLA Case Employee Request Detail", \
                    "FMLA Case Employee Work Segment Detail" \
                    ],
                  "Provisioning Reports", \
                    ["Employee Provisioning Detail", \
                    "Employee Provisioning Summary" \
                    ], \
                  ],
                "Scheduler Reports", \
                  ["Can make report public", \
                  "Change report options", \
                  "Change report settings", \
                  "Create saved reports", \
                  "Delete common saved reports", \
                  "Delete his/her own saved reports", \
                  "Edit common saved reports", \
                  "Edit his/her own saved reports", \
                  "Advanced Scheduler", \
                    ["Daily Shift", \
                    "Daily Shift Visual", \
                    "Employee Shift", \
                    "Offer Detail", \
                    "Open Shift", \
                    "Period Shift", \
                    "Scheduled Overtime", \
                    "Shift Validation", \
                    "Swap Request", \
                    "Monthly Shift Summary", \
                    "Drop Shift Request", \
                    "Expiring Qualification", \
                    "Master Shift Qualification", \
                    "Progressive Sequence" \
                    ],
                  "Automation", \
                    ["Edit", \
                    "Edit report automation run as User" \
                    ],
                  "Weekly", \
                    ["Weekly Schedule" \
                    ],
                  "Miscellaneous", \
                    ["Job Code Detail", \
                    "Availability", \
                    "Estimated Schedule Wages", \
                    "Requests", \
                    "Time Coverage" \
                    ],
                  "Daily Schedule", \
                    ["Daily Schedule", \
                    "Daily Visual Schedule" \
                    ],
                  "Individual", \
                    ["Individual Schedules" \
                    ],
                  "Job Code", \
                    ["Job Code Calendar", \
                    "Scheduled Job Code Analysis Detail", \
                    "Scheduled Job Code Analysis Summary" \
                    ], \
                  ],
                "Analytics", \
                  ["Compose", \
                  "Delete", \
                  "View" \
                  ], \
                ],
              "Tools", \
                ["Import", \
                  ["Create template", \
                  "Delete common saved templates", \
                  "Delete his/her saved templates", \
                  "Edit common saved templates", \
                  "Edit his/her saved templates", \
                  "Advanced scheduler shift assignments", \
                  "Budget Templates", \
                  "Job Code List", \
                  "Employee Information", \
                  "Employee Accruals", \
                  "Employee Budget Templates", \
                  "Employee Contracts", \
                  "Employee Job Code Information", \
                  "Employee Punches", \
                  "Employee Recurring Schedules", \
                  "Employee Requests", \
                  "Substitute Assignment", \
                  "Employee Role Job Codes", \
                  "Employee Roles", \
                  "Labor Analytics Demand Data", \
                  "Labor Cost Sales", \
                  "Location", \
                  "Master Schedules", \
                  "Master Shifts", \
                  "Rate Change History", \
                  "Recurring Schedules", \
                  "Recurring Schedule Segments", \
                  "Schedules", \
                  "Employee Segments", \
                  "Users", \
                  "Contract Information", \
                  "Employee Access", \
                  "Fingerprint - Digital Persona (Terminal)", \
                  "User Employee Access Filter", \
                  "Job Code Access", \
                  "Master Schedule Access", \
                  "Master Shift Access", \
                  "Employee Qualifications", \
                  "Occurrences", \
                  "Job Classes", \
                  "Qualifications", \
                  "Employee Work Profiles" \
                  ],
                "Export", \
                  ["Create template", \
                  "Delete common saved templates", \
                  "Delete his/her own saved templates", \
                  "Edit common saved templates", \
                  "Edit his/her own saved templates", \
                  "Advanced scheduler shift assignments", \
                  "Budget Templates", \
                  "Job Code List", \
                  "Employee Information", \
                  "Employee Accruals", \
                  "Employee Budget Templates", \
                  "Employee Contracts", \
                  "Employee Job Code Information", \
                  "Employee Recurring Schedules", \
                  "Employee Requests", \
                  "Employee Role Job Codes", \
                  "Employee Roles", \
                  "Labor Analytics Demand Data", \
                  "Labor Cost Sales", \
                  "Location", \
                  "Master Schedules", \
                  "Master Shifts", \
                  "Rate Change History", \
                  "Recurring Schedules", \
                  "Recurring Schedule Segments", \
                  "Schedules", \
                  "Employee Segments", \
                  "Contract Information", \
                  "User Cost Code Access", \
                  "User Employee Access Filter", \
                  "Users", \
                  "Fingerprint - Digital Persona (Terminal)", \
                  "Employee Qualifications", \
                  "Occurrences", \
                  "Job Classes", \
                  "Qualifications", \
                  "Employee Work Profiles", \
                  "Automation", \
                    ["Edit", \
                    "Edit export automation run as User" \
                    ], \
                  ],
                "Employee Status", \
                  ["Show employee id", \
                  "Show location in list", \
                  "View phone info", \
                  "View schedule info", \
                  "View shift info", \
                  "Edit Call Note (Requires View phone info)", \
                  "View", \
                    ["Absent", \
                    "All", \
                    "Attendance", \
                    "Auto Out", \
                    "Clocked In", \
                    "Hours", \
                    "Last Punch", \
                    "Leave", \
                    "Not In", \
                    "On Break", \
                    "Labor Standards" \
                    ],
                  "Clock Operations (Requires View Access)", \
                    ["Clock individuals in", \
                    "Clock individuals out", \
                    "Change job code" \
                    ], \
                  ],
                "Requests", \
                  ["Request Manager", \
                    ["Add", \
                    "Approve closed period", \
                    "Approve locked period", \
                    "Deny FMLA request", \
                    "Edit request", \
                    "Edit request detail", \
                    "Edit request after it has been approved", \
                    "Manage FMLA cases", \
                    "Manage leave group requests", \
                    "Manage own requests", \
                    "Manage requests that result in negative accrual balances", \
                    "Allow entering requests over usage cap", \
                    "Split unapproved time off request groups", \
                    "Merge unapproved time off requests and groups", \
                    "User can suppress employee notifications when adding requests", \
                    "User can suppress substitute notifications when adding requests", \
                    "User can suppress notifications when deleting requests", \
                    "View", \
                    "Allow request entry on restricted holidays", \
                    "Approve/Deny", \
                      ["Request Level 1", \
                      "Request Level 2", \
                      "Request Level 3", \
                      "Approve requests that are over the warning threshold", \
                      "Approve requests that are over the prevent or warning threshold", \
                      "Allow deny requests in job codes that prevent denial" \
                      ],
                    "Delete", \
                      ["Delete approved/denied requests", \
                      "Delete approved/denied requests in closed weeks", \
                      "Delete approved/denied requests in locked periods", \
                      "Delete canceled approved requests", \
                      "Delete canceled approved requests in closed weeks", \
                      "Delete canceled approved requests in locked periods", \
                      "Delete pending requests", \
                      "Delete pending requests in closed weeks", \
                      "Delete pending requests in locked periods", \
                      "Delete time sheets generated by request even if locked by system" \
                      ],
                    "Cancel", \
                      ["Cancel approved requests", \
                      "Cancel approved requests in closed weeks", \
                      "Cancel approved requests in locked periods" \
                      ], \
                    ],
                  "Substitute Assignment Manager", \
                    ["Delete", \
                    "Edit", \
                    "Manage Assigned Employee", \
                    "Merge Assignments", \
                    "Notify", \
                    "View", \
                    "Split Assignments", \
                    "Add", \
                      ["Add Covered Assignment", \
                      "Add Open Assignment" \
                      ],
                    "Long Term Assignments", \
                      ["Add", \
                      "Delete", \
                      "Edit", \
                      "View" \
                      ], \
                    ],
                  "Leave Bids", \
                    ["Add", \
                    "Delete", \
                    "View", \
                    "Close bids" \
                    ],
                  "FMLA Case Manager", \
                    ["Add", \
                    "Delete", \
                    "Edit", \
                    "Edit description", \
                    "Case Notes", \
                      ["Add", \
                      "Delete", \
                        ["Notes entered by other users", \
                        "Notes entered by self" \
                        ],
                      "Edit", \
                        ["Notes entered by other users", \
                        "Notes entered by self" \
                        ], \
                      ], \
                    ], \
                  ],
                "Labor Analytics Demand", \
                  ["View", \
                  "Edit" \
                  ],
                "Labor Cost", \
                  ["Worked", \
                  "Scheduled" \
                  ],
                "Documents", \
                  ["Document Categories", \
                    ["Add", \
                    "Edit", \
                    "Delete", \
                    "View" \
                    ],
                  "General Documents", \
                    ["Add", \
                    "Delete", \
                    "Download", \
                    "Edit", \
                    "View" \
                    ], \
                  ],
                "Qr Code Generator", \
                  ["Generate Configuration Type", \
                  "Generate Clock Operation" \
                  ],
                "Other Tools", \
                  ["Attendance Monitor", \
                    ["Option is visible to user" \
                    ],
                  "Audit Log", \
                    ["Attestations", \
                    "Biometric Attestation Status", \
                    "Biometric Confirmation", \
                    "Employee", \
                    "Incomplete Clock Operations", \
                    "User Delegation", \
                    "Temperature Score log", \
                    "Hours", \
                      ["View hours", \
                      "Segment Recovery" \
                      ], \
                    ],
                  "Notifications", \
                    ["Option is visible to user", \
                    "Resend Notifications" \
                    ],
                  "Unresolved Punches", \
                    ["Delete", \
                    "Import", \
                    "View" \
                    ],
                  "Data Purge", \
                    ["View" \
                    ],
                  "Calculator", \
                    ["Option is visible to user" \
                    ], \
                  ], \
                ],
              "Configuration", \
                ["Users", \
                  ["Edit dashboard template", \
                  "User Profiles", \
                    ["Add", \
                    "Allow creation of new user based on existing profile", \
                    "Copy", \
                    "Allow edit of other users Employee Access Filters", \
                    "Allow password change without current password (Requires the ""Change users password"" permission)", \
                    "Change general information", \
                    "Change users password", \
                    "Send password reset email", \
                    "Show temporary password on reset", \
                    "Change users access rights", \
                    "Change users job code access", \
                    "Change users covered employee access", \
                    "Change users employee access", \
                    "Change users Master Schedule Access", \
                    "Change users Master Shift Access", \
                    "Change users document access", \
                    "Apply dashboard template", \
                    "Delete", \
                    "View all users", \
                    "View users with same department", \
                    "Notifications", \
                    "Device Management", \
                      ["Edit", \
                      "View" \
                      ],
                    "Attestations", \
                      ["Assign", \
                      "Edit", \
                      "Revoke", \
                      "Unassign", \
                      "View" \
                      ], \
                    ],
                  "User Delegation", \
                    ["Delete", \
                    "View", \
                    "Add", \
                      ["User can delegate other users' access", \
                      "User can delegate own access" \
                      ],
                    "Edit", \
                      ["Change delegations last modified by other users", \
                      "Change delegations last modified by this user" \
                      ], \
                    ],
                  "User Roles", \
                    ["Manage role", \
                    "View role" \
                    ], \
                  ],
                "Job Codes", \
                  ["Add", \
                  "Delete", \
                  "Edit", \
                  "View" \
                  ],
                "Work Profiles", \
                  ["Add", \
                  "Delete", \
                  "Edit", \
                  "View" \
                  ],
                "Accruals", \
                  ["Accrual Bank", \
                    ["Add", \
                    "Delete", \
                    "Edit", \
                    "View" \
                    ],
                  "Accrual Rule", \
                    ["Add", \
                    "Delete", \
                    "Edit", \
                    "View" \
                    ],
                  "Accrual Cap Rules", \
                    ["Add", \
                    "Delete", \
                    "Edit", \
                    "View" \
                    ],
                  "Accrual Reset Rules", \
                    ["Add", \
                    "Delete", \
                    "Edit", \
                    "View" \
                    ],
                  "Leave Group", \
                    ["Add", \
                    "Delete", \
                    "Edit", \
                    "View" \
                    ],
                  "Leave Calendar", \
                    ["Add", \
                    "Delete", \
                    "Edit", \
                    "View" \
                    ], \
                  ],
                "Advanced Scheduler", \
                  ["Auto Fill Profiles", \
                    ["Add", \
                    "Delete", \
                    "Edit", \
                    "View", \
                    "Edit other users' private profiles", \
                    "View other users' private profiles" \
                    ],
                  "Master Schedules", \
                    ["Add", \
                    "Delete", \
                    "Edit", \
                    "View", \
                    "Allow ad hoc shifts", \
                    "User can create shift bid" \
                    ],
                  "Master Shifts", \
                    ["Add", \
                    "Copy requirement", \
                    "Delete", \
                    "Edit", \
                    "View" \
                    ],
                  "Offer Audit Log", \
                    ["View" \
                    ],
                  "Sequences", \
                    ["Add", \
                    "Delete", \
                    "Edit", \
                    "View" \
                    ],
                  "Swap Limits", \
                    ["Add", \
                    "Delete", \
                    "Edit", \
                    "View" \
                    ],
                  "Position Templates", \
                    ["Add", \
                    "Delete", \
                    "Edit", \
                    "View" \
                    ],
                  "Publisher", \
                    ["User can AutoFill", \
                    "User can AutoFill with other users' private profiles", \
                    "User can publish", \
                    "User can override existing segments when publishing", \
                    "User can override expired qualification exceptions when publishing", \
                    "User can unpublish", \
                    "User can remove swapped segments when unpublishing", \
                    "User can approve/deny publish event" \
                    ],
                  "Shift Bids", \
                    ["Add", \
                    "Delete", \
                    "Edit", \
                    "Finalize", \
                    "View", \
                    "User can assign master schedule positions", \
                    "User can assign master schedule shift defaults", \
                    "User can assign resource requirements", \
                    "User can view shift bid report" \
                    ], \
                  ],
                "Benefit Status", \
                  ["Measurement Periods", \
                    ["Add", \
                    "Delete", \
                    "Edit", \
                    "View" \
                    ],
                  "Break Period Groups", \
                    ["Add", \
                    "Delete", \
                    "Edit", \
                    "View" \
                    ], \
                  ],
                "Templates", \
                  ["Contract Templates", \
                    ["Add", \
                    "Delete", \
                    "Edit", \
                    "View", \
                    "Period Processing" \
                    ],
                  "Request Templates", \
                    ["Add", \
                    "Delete", \
                    "Edit", \
                    "View" \
                    ],
                  "Substitute Assignment Templates", \
                    ["Add", \
                    "Delete", \
                    "Edit", \
                    "View" \
                    ],
                  "Budget Templates", \
                    ["Add", \
                    "Delete", \
                    "Edit", \
                    "View" \
                    ], \
                  ],
                "FMLA", \
                  ["Questions", \
                    ["Add", \
                    "Delete", \
                    "Edit", \
                    "View" \
                    ],
                  "Reason Code", \
                    ["Add", \
                    "Delete", \
                    "Edit", \
                    "View" \
                    ], \
                  ],
                "Geofencing", \
                  ["Geofences", \
                    ["Add", \
                    "Delete", \
                    "Edit", \
                    "View" \
                    ],
                  "Geofence group", \
                    ["Add", \
                    "Delete", \
                    "Edit", \
                    "View" \
                    ], \
                  ],
                "Other Configurations", \
                  ["Clock Configurations", \
                    ["Add", \
                    "Delete", \
                    "Edit", \
                    "View", \
                    "Assign Employee Dashboard Templates", \
                    "Missed Punches" \
                    ],
                  "Shift Schedules", \
                    ["Add", \
                    "Delete", \
                    "Processing", \
                    "View", \
                    "Edit", \
                      ["Shift definitions", \
                      "Job adjustments" \
                      ], \
                    ],
                  "Automatic Breaks", \
                    ["Add", \
                    "Delete", \
                    "Edit", \
                    "View" \
                    ],
                  "User Options", \
                    ["User can change his/her own auto logoff", \
                    "User can change his/her own email address", \
                    "User can change his/her own sms address", \
                    "User can change his/her own password", \
                    "User can change his/her own SSO requirement", \
                    "User can change his/her own start in", \
                    "User can change his/her own show active items by default setting", \
                    "User can change his/her own remember latest date range setting", \
                    "User can change his/her own global filters", \
                    "Device Management", \
                      ["Edit", \
                      "View" \
                      ], \
                    ],
                  "PushNotifications", \
                    ["View", \
                    "Clear" \
                    ],
                  "Occurrence Rules", \
                    ["Add", \
                    "Delete", \
                    "Edit", \
                    "View" \
                    ],
                  "Rotating Overtime Schedules", \
                    ["Add", \
                    "Delete", \
                    "Edit", \
                    "View" \
                    ],
                  "Job Classes", \
                    ["Add", \
                    "Delete", \
                    "Edit", \
                    "View" \
                    ],
                  "Qualification", \
                    ["Add", \
                    "Delete", \
                    "Edit", \
                    "View" \
                    ],
                  "Location", \
                    ["Add", \
                    "Delete", \
                    "Edit", \
                    "View" \
                    ],
                  "Hours Calculation Priority Groups", \
                    ["Add", \
                    "Delete", \
                    "Edit", \
                    "View" \
                    ], \
                  ], \
                ],
              "Company", \
                ["Company Setup", \
                "Close Week", \
                  ["Close Week", \
                  "Undo close week" \
                  ],
                "Company Defaults", \
                  ["Global", \
                    ["Breaks", \
                      ["Edit", \
                      "View" \
                      ],
                    "Calculations", \
                      ["Edit", \
                      "View" \
                      ],
                    "Display Options", \
                      ["Edit", \
                      "View" \
                      ],
                    "Mail Settings", \
                      ["Edit", \
                      "View" \
                      ],
                    "Login Attempts", \
                      ["Edit", \
                      "View" \
                      ],
                    "Logout", \
                      ["Edit", \
                      "View" \
                      ],
                    "Check For Update", \
                      ["Edit", \
                      "View" \
                      ],
                    "Modules", \
                      ["Edit", \
                      "View" \
                      ],
                    "Password Policy", \
                      ["Edit", \
                      "View" \
                      ],
                    "Time Settings", \
                      ["Edit", \
                      "View" \
                      ],
                    "Workweek Finalizer", \
                      ["Edit", \
                      "View" \
                      ],
                    "Workday Adjustment", \
                      ["Edit", \
                      "View" \
                      ],
                    "Banner Integration", \
                      ["Edit", \
                      "View" \
                      ],
                    "PrismHR", \
                      ["Edit", \
                      "View" \
                      ],
                    "Occurrence Processing", \
                      ["Edit", \
                      "View" \
                      ],
                    "Server Url Settings", \
                      ["Edit", \
                      "View" \
                      ],
                    "Sub Search Plus App", \
                      ["Edit", \
                      "View" \
                      ],
                    "Manager Segment Approval Automation", \
                      ["Edit", \
                      "View" \
                      ],
                    "eFileCabinet", \
                      ["Edit", \
                      "View" \
                      ],
                    "Biometric Notice", \
                      ["Edit", \
                      "View" \
                      ],
                    "Real Time Data Sync", \
                      ["Edit", \
                      "View" \
                      ], \
                    ],
                  "Manager", \
                    ["Language", \
                      ["Edit", \
                      "View" \
                      ],
                    "Accruals", \
                      ["Edit", \
                      "View" \
                      ],
                    "Add Employee", \
                      ["Edit", \
                      "View" \
                      ],
                    "Employee Entry", \
                      ["Edit", \
                      "View" \
                      ],
                    "User Entry", \
                      ["Edit", \
                      "View" \
                      ],
                    "Close Week", \
                      ["Edit", \
                      "View" \
                      ],
                    "Segment Approvals", \
                      ["Edit", \
                      "View", \
                      "User can override required hour approvals" \
                      ],
                    "Occurrence Calculations", \
                      ["Edit", \
                      "View" \
                      ],
                    "System-Wide Search", \
                      ["Edit", \
                      "View" \
                      ],
                    "Advanced Scheduler", \
                      ["Edit", \
                      "View" \
                      ], \
                    ],
                  "Scheduler", \
                    ["Transfer Schedule Information", \
                      ["Edit", \
                      "View" \
                      ],
                    "Configure Schedule Exception Processing", \
                      ["Edit", \
                      "View" \
                      ],
                    "On Call Schedule Transfer", \
                      ["Edit", \
                      "View" \
                      ], \
                    ],
                  "Client", \
                    ["Employee ID Preference", \
                      ["Edit", \
                      "View" \
                      ],
                    "Miscellaneous", \
                      ["Edit", \
                      "View" \
                      ],
                    "Log On Settings", \
                      ["Edit", \
                      "View" \
                      ],
                    "Clock Operation Labels", \
                      ["Edit", \
                      "View" \
                      ],
                    "Missed Punches", \
                      ["Edit", \
                      "View" \
                      ],
                    "Request Entry", \
                      ["Edit", \
                      "View" \
                      ],
                    "Request Processing", \
                      ["Edit", \
                      "View" \
                      ],
                    "Advanced Scheduler", \
                      ["Edit", \
                      "View" \
                      ],
                    "Substitute Module", \
                      ["Edit", \
                      "View" \
                      ],
                    "Access Restrictions", \
                      ["Edit", \
                      "View" \
                      ], \
                    ],
                  "LDAP", \
                    ["Edit", \
                    "View" \
                    ],
                  "Report", \
                    ["Edit report footer", \
                    "View report footer" \
                    ],
                  "Tokenization", \
                    ["Edit", \
                    "View" \
                    ],
                  "Notification", \
                    ["Advanced Scheduler Notification", \
                      ["Edit", \
                      "View" \
                      ],
                    "Clock Operation Notification", \
                      ["Edit", \
                      "View" \
                      ],
                    "RDTg Connection Notification", \
                      ["Edit", \
                      "View" \
                      ],
                    "Push Notification Automation", \
                      ["Edit", \
                      "View" \
                      ],
                    "Request Notification", \
                      ["Edit", \
                      "View" \
                      ],
                    "Recent Exception Notifications", \
                      ["Edit", \
                      "View" \
                      ],
                    "Occurrence Threshold Notifications", \
                      ["Edit", \
                      "View" \
                      ],
                    "Actionable notifications", \
                      ["Edit", \
                      "View" \
                      ],
                    "Scheduled Clock In Notification", \
                      ["Edit", \
                      "View" \
                      ],
                    "User Delegation Notification", \
                      ["Edit", \
                      "View" \
                      ],
                    "Questions On Clock Operations Notifications", \
                      ["Edit", \
                      "View" \
                      ],
                    "Leave Bid Notifications", \
                      ["Edit", \
                      "View" \
                      ],
                    "FMLA Notifications", \
                      ["Edit", \
                      "View" \
                      ],
                    "Budget Threshold Notification", \
                      ["Edit", \
                      "View" \
                      ],
                    "Employee Deletion Notification", \
                      ["Edit", \
                      "View" \
                      ],
                    "Employee Recovery Notification", \
                      ["Edit", \
                      "View" \
                      ], \
                    ],
                  "FMLA Settings", \
                    ["Edit", \
                    "View" \
                    ], \
                  ],
                "Company Template", \
                  ["Access" \
                  ],
                "Custom Fields", \
                  ["Add", \
                  "Delete", \
                  "Edit", \
                  "View" \
                  ],
                "Holidays", \
                  ["Add", \
                  "Delete", \
                  "Edit", \
                  "View" \
                  ],
                "Automated Tasks", \
                  ["Add", \
                  "Delete", \
                  "Edit", \
                  "Start", \
                  "Stop", \
                  "View", \
                  "Automation Modules", \
                    ["View", \
                    "Edit" \
                    ],
                  "Imports", \
                    ["Automated Import" \
                    ], \
                  ],
                "Attestations", \
                  ["Add", \
                  "Delete", \
                  "Edit", \
                  "View" \
                  ],
                "Embeddable Widgets", \
                  ["Add", \
                  "Delete", \
                  "Edit", \
                  "View" \
                  ], \
                ], \
              ],
            "Clocks", \
              ["Clock Badge Enrollment (300/400 series and Ultima Kiosk only)", \
              "Handscanner management feature menu", \
              "Face Scanner", \
              "Face Scanner User Enrollment", \
              "Fingerprint Management", \
              "Manage Kiosk", \
              "Manage Terminals", \
                ["Add", \
                "Edit", \
                "Delete", \
                "View" \
                ],
              "Manage Hardware Extension Configurations", \
                ["Add", \
                "Edit", \
                "Delete", \
                "View" \
                ],
              "Manage Hardware Extension Data", \
                ["Delete", \
                "View" \
                ], \
              ],
            "Workstation Hub", \
              ["Workstation Hub", \
                ["Fingerprints", \
                  ["Add", \
                  "Delete", \
                  "View" \
                  ] \
                ] \
              ] \
            ]
          ]
        ],        
     
      "User Roles", \
      "Security Check", \
      "Dashboard Templates", \
      "User Delegation"
      ], \
    "Job Codes", \
      ["General", \
        ["Information", \
          ["Number", \
          "Description", \
          "Group", \
          "Location", \
          "Geofence Group", \
          "Job Class", \
          "Import ID", \
          "Leave Code", \
          "Prevent denial of leave requests", \
          "Supplemental Hours", \
          "FMLA Code", \
          "Include in FMLA eligibility", \
          "Include in Benefit Status", \
          "Start date", \
          "Stop date" \
          ], \
        "Defaults", \
          ["Clockable", \
          "Ask for a cost code", \
          "Ask for labor codes", \
          "Distribute segment time across labor codes", \
          "Apply full segment time to each labor code", \
          "Auto transfer hours from schedule during close week", \
          "Auto transfer hours from schedule at scheduled time", \
          "Process shift differential", \
          "Do not pay", \
          "Substitute job code", \
          "No Overtime 1", \
          "Counts Overtime 1", \
          "Earns Overtime 1", \
          "No Overtime 2", \
          "Counts Overtime 2", \
          "Earns Overtime 2", \
          "Do not force overtime", \
          "Force overtime 1", \
          "Force overtime 2", \
          "No comp time", \
          "Counts toward comp time", \
          "Earns comp time", \
          "Default to normal pay", \
          "Default to comp time", \
          "Allow toggling comp time", \
          "Force comp time", \
          "Default pay rate", \
          "Allow time sheet entry", \
          "Allow Add", \
          "Flag time-based segments as missed punches", \
          "Allow Edit", \
          "Allow Delete" \
          ], \
        "Cost Code Groups", \
          ["No records found" \
          ], \
        "Tracked Fields", \
          ["Display ONS", \
          "Include in Weighted Overtime", \
          "Display 47", \
          "Include in Weighted Overtime", \
          "Display Track3", \
          "Include in Weighted Overtime" \
          ], \
        "Requests", \
          ["Override employee settings", \
          "Require request level 1 approval for requests", \
          "Require request level 2 approval for requests", \
          "Require request level 3 approval for requests" \
          ], \
        "FMLA", \
          ["Allow employee to add to leave usage schedule", \
          "Allow employee to remove from leave usage schedule" \
          ] \
        ] \
      ], \
    "Cost Codes", \
      ["Cost Code Simple Select", \
      "Cost Code List", \
      "Cost Code Tree", \
      "Cost Code Groups", \
      "Cost Code Elements", \
      "Labor Standards"
      ], \
    "Work Profiles", \
    "Accruals", \
      ["Accrual Banks", \
      "Accrual Cap Rules", \
      "Accrual Reset Rules", \
      "Accrual Rules", \
      "Leave Groups", \
      "Leave Calendars"
      ], \
    "Advanced Scheduler", \
      ["AutoFill Profiles", \
      "Master Shifts", \
      "Master Schedules", \
      "Shift Bids", \
      "Sequences", \
      "Swap Limits", \
      "Position Templates", \
      "Publisher"
      ], \
    "Templates", \
      ["Contract Templates", \
      "Request Templates", \
      "Substitute Assignment Templates", \
      "Budget Templates"
      ], \
    "Benefit Status", \
      ["Measurement Periods", \
      "Break Period Groups"
      ], \
    "FMLA", \
      ["Reason Codes", \
      "Questions"
      ], \
    "Geofencing", \
      ["Geofences", \
      "Geofence Groups"
      ], \
    "Other Configurations", \
      ["Clock Configurations", \
      "Shift Schedules", \
      "Automatic Breaks", \
      "Occurrence Rules", \
      "Rotating Overtime Schedules", \
      "Job Classes", \
      "Qualifications", \
      "Locations", \
      "Hour Calculation Priority Groups"
      ]
    ], \
  "Company", \
    ["Close Week", \
    "Company Defaults", \
      ["Global", \
        ["Display Options", \
          ["Display Name", \
          "Company Name", \
          "Roster", \
          "Leave segment background color", \
          "Leave segment text color", \
          "Leave segment border color", \
          "Non shift segment background color", \
          "Non shift segment text color", \
          "Non shift segment border color", \
          "Tracked Fields", \
          "Enable tracked fields", \
          "Tracked field 1 name", \
          "Include in Weighted Overtime", \
          "Tracked field 2 name", \
          "Include in Weighted Overtime", \
          "Tracked field 3 name", \
          "Include in Weighted Overtime", \
          "Display Formats", \
          "Time format", \
          "Date format", \
          "Hour format", \
          "Precision", \
          "Accruals Format", \
          "Precision", \
          "Rate precision", \
          "Currency format" \
          ], \
        "Calculations", \
          ["Calculate hours counting toward overtime but not earning overtime first", \
          "Calculate hours counting toward comp time but not earning comp time first", \
          "Calculate contract hours counting towards overtime first", \
          "Include shift differential premium in base rate when calculating overtime", \
          "Reset forced overtime flags when processing shift differential", \
          "Flag time sheet segments as conflict when start time is the same as a worked segment", \
          "Calculate contract hours in order of hour type", \
          "Track straight overtime", \
          "How do forced overtime segments count toward overtime", \
          "How do forced comp time segments count toward comp time", \
          "How many hours constitute a day worked", \
          "Include non-clockable hours", \
          "Maximum length of a worked segment", \
          "Also restrict time sheets", \
          "Current week", \
          "Bi-weekly base date", \
          "Quad weekly base date", \
          "Pay period" \
          ], \
        "Breaks", \
          ["Break type", \
          "Active", \
          "A long break is longer than", \
          "A short break is shorter than", \
          "Round breaks to nearest", \
          "Round first 0 minutes up at", \
          "Round other 0 minutes up at", \
          "Break type", \
          "Active", \
          "A long break is longer than", \
          "A short break is shorter than", \
          "Round breaks to nearest", \
          "Round first 0 minutes up at", \
          "Round other 0 minutes up at", \
          "Break type", \
          "Active", \
          "A long break is longer than", \
          "A short break is shorter than", \
          "Round breaks to nearest", \
          "Round first 0 minutes up at", \
          "Round other 0 minutes up at", \
          "Break type", \
          "Active", \
          "A long break is longer than", \
          "A short break is shorter than", \
          "Round breaks to nearest", \
          "Round first 0 minutes up at", \
          "Round other 0 minutes up at", \
          "Break type", \
          "Active", \
          "A long break is longer than", \
          "A short break is shorter than", \
          "Round breaks to nearest", \
          "Round first 0 minutes up at", \
          "Round other 0 minutes up at", \
          "Maximum number of minutes between segments that is still considered a break", \
          "(1 - 240)", \
          "Time of day based", \
          "Length-based" \
          ], \
        "Paid Break Limit", \
          ["Group 1", \
          "Group 2", \
          "Group 3", \
          "Group 4", \
          "No records found", \
          "Lunch", \
          "Lunch", \
          "Break3", \
          "Breakfive", \
          "Break5" \
          ], \
        "Cost Codes", \
          ["Status 1", \
          "Status 2", \
          "Status 3", \
          "Status 4", \
          "Status 5", \
          "Status 6", \
          "Status 7", \
          "Status 8", \
          "Status 9", \
          "Status 10", \
          "User defined field 1", \
          "User defined field 2", \
          "User defined field 3", \
          "User defined field 4", \
          "Level 1", \
          "Level 2", \
          "Level 3", \
          "Level 4", \
          "Level 5", \
          "Intersection (cost codes must be in all groups)", \
          "Union (cost codes can be in any group)" \
          ], \
        "Password Policy", \
          ["System Access", \
          "WebClock Override", \
          "Clock Edit Hours", \
          "Clock Override", \
          "Employee Password", \
          "No records found", \
          "Allow users to self reset password via email.", \
          "Employees must change password after manual update" \
          ], \
        "Login Attempts", \
          ["Prevent multiple unsuccessful login attempts", \
          "consecutive unsuccessful attempts within", \
          "minutes will lock the user for", \
          "Email when login attempts are exceeded" \
          ], \
        "Logout", \
          ["Employee URL", \
          "User URL" \
          ], \
        "Time Settings", \
          ["Time zone", \
          "Automatically adjust hours for daylight savings", \
          "Time Offset", \
          "Display scheduled time on calendar day" \
          ], \
        "Mail Settings", \
          ["SMTP server", \
          "SMTP port number", \
          "Reply to address", \
          "Have all system generated emails come from the ""Reply to address""", \
          "Enable encryption (TLS)", \
          "Outbound server requires authentication", \
          "User name", \
          "Update password (Password is not blank)", \
          "Password", \
          "Re-enter password", \
          "Test email address" \
          ], \
        "Contracts First", \
        "Daily Overtime Exemption", \
          ["Disable daily overtime on segments that meet or exceed the exemption threshold", \
          "Disable daily overtime on shifts that meet or exceed the exemption threshold", \
          "Exemption threshold", \
          "Exclude segments that are forced to overtime 1", \
          "Exclude segments that are forced to overtime 2", \
          "Exclude segments with 6th consecutive day overtime", \
          "Exclude segments with 7th consecutive day overtime", \
          "Exclude holiday hours" \
          ], \
        "Floating Pay Period", \
          ["Period base date", \
          "Period length", \
          "days" \
          ], \
        "Forced Overtime", \
          ["Sunday", \
          "Forced overtime starts at", \
          "Monday", \
          "Forced overtime starts at", \
          "Tuesday", \
          "Forced overtime starts at", \
          "Wednesday", \
          "Forced overtime starts at", \
          "Thursday", \
          "Forced overtime starts at", \
          "Friday", \
          "Forced overtime starts at", \
          "Saturday", \
          "Forced overtime starts at", \
          "Override calculations for days that are marked as a holiday", \
          "Override calculation for days that are calculated as 6th consecutive day overtime", \
          "Override calculation for days that are calculated as 7th consecutive day overtime", \
          "Include segments that are configured to not earn overtime" \
          ], \
        "Include Overtime In Regular Hours", \
          ["Process when reporting", \
          "Process when exporting" \
          ], \
        "Salaried Non-Exempt", \
          ["Round rates to company specified precision after calculation" \
          ], \
        "Weighted Overtime", \
          ["Weighted Base Rate: All WagesAll Hours OTRate=RegRate x Factor", \
          "Weighted Overtime Rate: RegRate=No Change OTRate=RegRate+(Weighted Factor)", \
          "Weighted Overtime Rate: RegRate=No Change OTRate=Weighted Base x Factor", \
          "Redistribute overtime hours to each job code worked", \
          "For base rate calculation wages are determined by calculating the sum of all unique regular rates times the number of hours worked in that rate", \
          "Calculate on a weekly basis even if employee is bi-weekly or quad-weekly", \
          "Process calculations when exporting data", \
          "Process calculations when generating reports", \
          "Include rate of pay when determining job code groups for redistribution of hours", \
          "Distribute overtime for shift segments that are forced to overtime", \
          "Distribute overtime to shift segments that do not earn overtime", \
          "Distribute overtime to end of distribution period first", \
          "Round weighted rate up to the nearest cent" \
          ], \
        "Workweek Finalizer", \
          ["Enable workweek finalizer", \
          "Minimum hours", \
          "Default hours", \
          "Include leave in minimum calculation", \
          "Job Code", \
          "Leave Group", \
          "Process employees even if they have no hours", \
          "Process weeks if they result in negative accruals", \
          "Process all completed open weeks up to 8 weeks.", \
          "Exclude terminated and suspended employees", \
          "Add time sheet hours at the last minute of the week", \
          "Add time sheet hours after the end of the last segment worked", \
          "Send an email upon completion of processing", \
          "Send an email even if no changes are made" \
          ], \
        "Segment Post Processor (STA)", \
          ["Segment minimum" \
          ], \
        "Missed Break", \
          ["Process Shift", \
          "Up to previous day", \
          "Up to current day", \
          "minutes without break", \
          "cumulative break threshold", \
          "Count Minutes", \
          "All segments up to first disabled job code or break", \
          "First segment only", \
          "Segment Placement", \
          "First minute of shift", \
          "Last minute of shift", \
          "First minute of day", \
          "Last minute of day", \
          "Job Code", \
          "Time", \
          "Use segment cost code" \
          ], \
        "Split Segment Automation", \
        "Split To Schedule", \
          ["Send an email upon completion of processing" \
          ], \
        "Split By Percentage", \
          ["Apply automatic breaks before split", \
          "Only process segments with other approval", \
          "Send an email upon completion of processing", \
          "Only notify of failures" \
          ], \
        "Banner Integration Automation", \
        "PrismHR", \
          ["Employee authentication URL", \
          "User authentication URL", \
          "Url", \
          "Client ID", \
          "PEO ID", \
          "User ID", \
          "Username", \
          "Use accrual subscriptions", \
          "Update password (Password is blank)", \
          "Password", \
          "Re-enter password", \
          "Sync employee work email instead of personal email" \
          ], \
        "Incident Report", \
          ["Reporting period", \
          "Period", \
          "Period start offset", \
          "days", \
          "Period stop offset", \
          "days", \
          "Accrual Bank" \
          ], \
        "Supplemental Hours", \
          ["Select job code", \
          "Add additional time before first shift of the day", \
          "Add additional time after last shift of the day (Not recommended for 24 hour companies)", \
          "Add additional time at", \
          "Ranges", \
          "No records found" \
          ], \
        "Shift Differential Minimum", \
          ["Minimum required to get premiums", \
          "Last shift grace period", \
          "Ignore individuals that do not have shift differential enabled" \
          ], \
        "Segment Rounding Automation", \
          ["Send an email upon completion of processing", \
          "Only notify of failures", \
          "Include Current Day", \
          "Round missed punches", \
          "Save original punch time in actual times", \
          "Round up at minutes", \
          "Round to minutes" \
          ], \
        "Start Time Shift Adjustment Processing", \
          ["Percentage" \
          ], \
        "Automated Segment Entry - Long Break Fill", \
        "Automated Segment Entry - Clock In Fill", \
          ["Window Start", \
          "Window Stop", \
          "Job Code" \
          ], \
        "Namely", \
          ["Employee authentication URL", \
          "User authentication URL", \
          "Client ID", \
          "Client Secret" \
          ], \
        "Spread of Hours", \
          ["Hour threshold", \
          "Additional time", \
          "Job Code", \
          "At the start of the first shift of the day", \
          "At the end of the last shift of the day", \
          "At a specific time during the day" \
          ], \
        "West Park Automation", \
        "Occurrence Processing", \
        "Variable Leave Segment Processing", \
          ["Both add and remove leave", \
          "Add leave", \
          "Remove leave" \
          ], \
        "Persisted Calculations Automation", \
        "Server URL Settings", \
          ["External server URL" \
          ], \
        "Cost Code Expiration Automation", \
          ["Reactivate inactive cost codes with future expiration date" \
          ], \
        "Manager Segment Approval Automation", \
          ["Require employee approval and no changes to segment within the last", \
          "Require segments to be exactly", \
          "hours in length", \
          "Exclude Time Sheets", \
          "Require segments to be non leave job codes", \
          "User for approvals:" \
          ], \
        "Threshold Based Job Code Adjustment Automation", \
          ["Hour threshold" \
          ], \
        "Split Hours Over Contract Automation", \
        "Salaried Exempt Automation", \
        "SubSearch Plus App", \
        "eFileCabinet", \
          ["Username", \
          "Update password (Password is blank)", \
          "Password", \
          "Re-enter password" \
          ], \
        "Biometric Notice", \
          ["Enable biometric notice" \
          ] \
        ] \
      ],
    "Company Setup", \
    "Company Template", \
    "Custom Fields", \
    "Holidays", \
    "Automated Tasks", \
      ["Manage Automated Task", \
      "Automated Import", \
      "Automation Modules"
      ], \
    "Certificates", \
    "Embeddable Widgets"
    ], \
  "On-Demand Pay", \
    ["About Clair On-Demand Pay", \
    "Settings"
    ], \
  "Quick Links", \
    ["Employee Profiles", \
    "Leave Groups", \
    "Request Templates", \
    "Clock Configurations"
    ]
  ]
]

window = tk.Tk()
window.resizable()

def get_previous_final_path_str(final_path_str):
  new_str = final_path_str
  last_caret_found = False
  for i in range(len(final_path_str) - 1,1,-1):
    curr_char = final_path_str[i]
    
    if last_caret_found == False:
      if curr_char == ">":
        last_caret_found = True
    else:
      if curr_char != " ":
        new_str = final_path_str[0:i + 1]
        return new_str
  return new_str

def get_previous_ary_path(ary_path):
  new_str = ary_path
  for i in range(len(ary_path) - 1,1,-1):
    curr_char = ary_path[i]
    match curr_char:
      case "[":
        new_str = ary_path[0:i]
        return new_str
  return new_str

def load_page_buttons(ary_path, curr_element, final_path_str, direction="forward"):
  if direction == "back":
    ary_path = get_previous_ary_path(ary_path)
    final_path_str = get_previous_final_path_str(final_path_str)
    

  if ary_path == '[1]':
    final_path_str = curr_element
  elif direction == "back":
    None
  else:
    final_path_str = final_path_str + ' > ' + curr_element
  # clear previous buttons
  for widget in window.winfo_children():
    widget.destroy()

  print(ary_path)
  print(final_path_str)  
  
  # entry box holds final path string for user viewing and copy
  lbl = tk.Entry(width=250)
  lbl.pack()
  lbl.insert(0,final_path_str)

  #copy button
  btn_copy = tk.Button(text="copy", command=pyperclip.copy(lbl.get()))
  btn_copy.pack()

  # start over button
  btn_restart = tk.Button(text="start over", command=lambda : load_page_buttons('', '', '','forward'))
  btn_restart.pack()
  
  # back one level button
  btn_back = tk.Button(text="back one level", command=lambda : load_page_buttons(ary_path, '', final_path_str,'back'))
  btn_back.pack()  


  # exit button
  btn_exit = tk.Button(text="exit", command=sys.exit)
  btn_exit.pack()




  try:
    curr_ary_full = eval('ary_menu' + ary_path)
  except:
    print(final_path_str)
  else:
    if isinstance(curr_ary_full,str):
      print(final_path_str)
    else:
      for i in range(0,len(curr_ary_full)):
        curr_element = curr_ary_full[i]
        if isinstance(curr_element,str):
          ary_path_str = ary_path + "[" + str(i + 1) + "]"
          btn0 = tk.Button(text = curr_element, command=lambda \
            ary_path_str = ary_path_str, \
            curr_element = curr_element, \
            final_path_str = final_path_str : \
            load_page_buttons(ary_path_str, curr_element,final_path_str))
          btn0.pack()

load_page_buttons('', '', '','forward')


window.mainloop()
