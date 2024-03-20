function abrir_sidebar(){
    document.getElementById('open_btn').addEventListener('click', function(){
        document.getElementById('sidebar').classList.toggle('open-sidebar');
    });
}
abrir_sidebar()

function adiciona_cor() {
   document.getElementById('side_items').addEventListener('click', function(){
    document.getElementsByClassName('side_item').classList.add('active')
   })
}
adiciona_cor()