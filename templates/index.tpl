<!DOCTYPE html>
<html>
  <head>
    <script type="text/javascript" src="/assets/javascript/jquery-1.8.2.min.js"></script>
  </head>
  <body>
    <p>The open items are as follows:</p>
    <table border="1">
    %for row in rows:
      <tr>
      %for col in row:
        <td>{{col}}</td>
      %end
      </tr>
    %end
    </table>
  </body>
</html>