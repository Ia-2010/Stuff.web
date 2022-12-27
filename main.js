function compute() {
    var data = document.getElementById("data").value
    eel.demo(data)(setValue)
    compute(); 
    // call the demo function which we have created in the main.py file
    eel.oo()

}

function setValue(res) {
    document.getElementById("abc").src = res
}



