import React from 'react';
import axios from 'axios';
import ReactTable from "react-table";
import 'react-table/react-table.css';


class Connections extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            connections: [],
            loading: true
        }
    }

    async getConnectionsData() {
        try {
            const res = await axios.get('http://localhost:5000/api/v1/connection')
            this.setState({ loading: false, connections: res.data })
        } catch {
            console.error("Could not get connections")
        }
    }

    componentDidMount() {
        this.getConnectionsData()
    }

    render() {
        const columns = [
            {
                Header: 'ID',
                accessor: 'id',
            },
            {
                Header: 'Name',
                accessor: 'name',
            }
        ]
        console.log(this.state.connections)
        return (
                <ReactTable
                    data={this.state.connections}
                    columns={columns}
                />
        );
    }
}

export default Connections;