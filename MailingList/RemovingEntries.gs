function myFunction() {
  //sheets from file
  const mailingSheet = SpreadsheetApp.getActive().getSheetByName("Mailing_List");
  const removeEmailSheet = SpreadsheetApp.getActive().getSheetByName("Remove_Email");

  //array of email entries from each sheet
  var emailToRemove = removeEmailSheet.getRange('B:B').getValues();
  var mailingListEmails = mailingSheet.getRange('C:C').getValues();
  
  //finds matching email entries from the remove email sheet and deletes entries from both the mailling list and remove email list sheet
  var i = 0;
  var j = 0;
  while(emailToRemove[i] != '')
  {
    while(mailingListEmails[j] != '')
    {
      if(mailingListEmails[j].toString() == emailToRemove[i].toString())
      {
        mailingSheet.deleteRow(j+1);
        removeEmailSheet.deleteRow(i+1);
      }
      j++;
    }
    i++;
    j = 0;
  }

  //removes all extra entries from the remove email list (these entries if not matching are considered false entries)
  i = 1;
  while(emailToRemove[i] != '')
  {
    removeEmailSheet.deleteRow(i+1);
  }
}